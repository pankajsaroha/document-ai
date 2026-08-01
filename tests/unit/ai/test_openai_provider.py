from unittest.mock import MagicMock
import pytest

from app.ai.models import (
    ChatRequest,
    Message,
    RequestContext,
    Role,
    TextPart
)
from app.ai.openai_provider import OpenAIProvider
from app.core.settings import Settings

from openai import APIConnectionError, RateLimitError
from app.ai.exceptions import RateLimitError as ProviderRateLimitError

# Fixtures

@pytest.fixture
def settings():
    return Settings(
        openai_api_key="fake-key",
        openai_model="gpt-5"
    )

@pytest.fixture
def mock_client():
    return MagicMock()

@pytest.fixture
def provider(settings, mock_client):
    return OpenAIProvider(
        settings=settings,
        client=mock_client
    )

@pytest.fixture
def text_message():
    return Message(
        role=Role.USER,
        parts=[
            TextPart(
                text="hello"
            )
        ]
    )

@pytest.fixture
def chat_request(text_message):
    return ChatRequest(
        messages=[text_message],
        context=RequestContext(
            request_id="req-1",
            user_id="user-1",
            session_id="session-1",
            tags={},
        ),
        requested_at = None
    )

# test _build_message

def test_build_message(provider, chat_request):
    messages = provider._build_messages(chat_request)

    assert messages == [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "hello"
                }                
            ]
        }
    ]

# test successful chat()

def test_chat_success(provider, chat_request, mock_client):
    mock_choice = MagicMock()
    mock_choice.message.content = "Hi there!"
    mock_choice.finish_reason = "stop"

    mock_usage = MagicMock()
    mock_usage.prompt_tokens = 10
    mock_usage.completion_tokens = 5
    mock_usage.total_tokens = 15

    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    mock_response.model = "gpt-5"
    mock_response.id = "resp-123"
    mock_response.created = 123456789
    mock_response.usage = mock_usage

    mock_client.chat.completions.create.return_value = mock_response

    response = provider.chat(chat_request)
    
    assert response.content == "Hi there!"
    assert response.model == "gpt-5"
    assert response.finish_reason == "stop"

    assert response.response_id == "resp-123"

    assert response.usage.prompt_tokens == 10
    assert response.usage.completion_tokens == 5
    assert response.usage.total_tokens == 15

    mock_client.chat.completions.create.assert_called_once()

# test model override

def test_chat_uses_request_model(
    provider, chat_request, mock_client
):
    chat_request.model = "gpt-4.1"

    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(
            message = MagicMock(content="hello"),
            finish_reason = "stop"
        )
    ]
    mock_response.id = "resp-123"
    mock_response.model = "gpt-4.1"
    mock_response.create = 1
    mock_response.usage = None

    mock_client.chat.completions.create.return_value = mock_response

    provider.chat(chat_request)

    _, kwargs = mock_client.chat.completions.create.call_args

    assert kwargs["model"] == "gpt-4.1"

# test default model

def test_chat_usage_default_model(provider, chat_request, mock_client):
    chat_request.model = None

    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(
            message=MagicMock(content="hello"),
            finish_reason="stop"
        )
    ]
    mock_response.model = "gpt-5"
    mock_response.create = 1
    mock_response.response_id = "resp-1"
    mock_response.usage = None

    mock_client.chat.completions.create.return_value = mock_response

    provider.chat(chat_request)

    _, kwargs = mock_client.chat.completions.create.call_args

    assert kwargs["model"] == "gpt-5"

# test health check

def test_health_success(provider, mock_client):
    mock_client.models.list.return_value = []
    assert provider.health() is True

def test_health_failure(provider, mock_client):
    mock_client.models.list.side_effect = APIConnectionError(
        request = MagicMock()
    )

    assert provider.health() is False

# test exception translation

def test_chat_translates_rate_limit_error(provider, chat_request, mock_client):
    mock_client.chat.completions.create.side_effect = (
        RateLimitError(
            message="Too many request",
            response=MagicMock(),
            body={}
        )
    )

    with pytest.raises(ProviderRateLimitError):
        provider.chat(chat_request)
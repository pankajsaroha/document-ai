from datetime import datetime, timedelta

from app.ai.models import (
    ChatRequest, 
    ChatResponse,
    Message,
    RequestContext,
    Role,
    TextPart,
    TokenUsage
)

def test_text_part():
    part = TextPart(
        text = "hello"
    )

    assert part.text == "hello"

def test_message():
    message = Message(
        role = Role.USER,
        parts = [
            TextPart(
                text = "hello"
            )
        ]
    )

    assert message.role == Role.USER
    assert len(message.parts) == 1
    assert message.parts[0].text == "hello"

def test_request_context():
    context = RequestContext(
        request_id = "req-123",
        user_id = "user-1",
        session_id = "session-1"
    )

    assert context.request_id == "req-123"
    assert context.user_id == "user-1"
    assert context.session_id == "session-1"
    assert context.tags == {}

def test_chat_request():
    request = ChatRequest(
        messages = [
            Message (
                role = Role.USER,
                parts = [
                    TextPart(
                        text = "hello"
                    )
                ]
            )
        ],
        context = RequestContext(
            request_id = "req-1"
        ),
        requested_at = datetime.now(),
        timeout = timedelta(seconds=30)
    )

    assert len(request.messages) == 1
    assert request.model is None
    assert request.temperature == 0.0
    assert request.timeout == timedelta(seconds=30)

def test_token_usage():
    usage = TokenUsage(
        prompt_tokens = 10,
        completion_tokens = 20,
        total_tokens = 30
    )

    assert usage.prompt_tokens == 10
    assert usage.completion_tokens == 20
    assert usage.total_tokens == 30

def test_chat_response():
    response = ChatResponse(
        content = "hello",
        model = "gpt-5",
        provider = "openai",
        response_id = "resp-1",
        created_at = datetime.now(),
        usage = None
    )

    assert response.content == "hello"
    assert response.model == "gpt-5"
    assert response.provider == "openai"
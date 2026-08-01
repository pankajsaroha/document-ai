import pytest

from app.ai.factory import AIProviderFactory
from app.ai.openai_provider import OpenAIProvider
from app.core.settings import Settings

def test_create_openai_provider():
    
    settings = Settings(
        ai_provider = "openai",
        openai_api_key = "fake-key"
    )

    provider = AIProviderFactory.create(settings)

    assert isinstance(provider, OpenAIProvider)

def test_unsupported_provider():

    settings = Settings(
        ai_provider = "gemini"
    )

    with pytest.raises(ValueError) as ex:
        AIProviderFactory.create(settings)

    assert "Unsupported AI Provider" in str(ex.value)
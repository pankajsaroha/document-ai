from app.ai.openai_provider import OpenAIProvider
from app.ai.provider import AIProvider

from openai import OpenAI

from app.core.settings import Settings

class AIProviderFactory:

    @staticmethod
    def create(settings: Settings) -> AIProvider:

        match settings.ai_provider.lower():

            case "openai":
                client = OpenAI(api_key=settings.openai_api_key)
                return OpenAIProvider(settings, client)

            case _:
                raise ValueError(
                    f"Unsupported AI Provider: {settings.ai_provider}"
                )
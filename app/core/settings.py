from pydantic import SecretStr
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from app.core.enums import AIProvider
from app.core.enums import Environment


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables or .env.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="DOCUMENT_AI_",
        case_sensitive=False,
        extra="ignore",
    )

    environment: Environment = Environment.DEVELOPMENT

    log_level: str = "INFO"

    app_name: str = "Document AI"
    app_version: str = "0.1.0"

    ai_provider: AIProvider = AIProvider.OPENAI

    openai_api_key: SecretStr | None = None # print(settings) will show open_api_key=sk-xxxxxx due to SecretStr
    openai_model: str = "gpt-5"
# Load configuration -> Validate configuration -> Expose immutable settings

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.constants import (
    DEFAULT_ENVIRONMENT,
    DEFAULT_LOG_LEVEL,
)

class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables or .env file.

    Every configuration value must originate here.
    """

    environment: str = Field(default=DEFAULT_ENVIRONMENT, env="development")
    
    log_level: str = Field(default=DEFAULT_LOG_LEVEL)
    
    app_name: str = Field(default="Document AI")

    app_version: str = Field(default="0.1.0")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix = "DOCUMENT_AI_",
        case_sensitive=False,
        extra="ignore",
    )
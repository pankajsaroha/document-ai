# heart of the app

from pathlib import Path

from app.application.application import Application
from app.application.banner import StartupBanner
from app.application.health import HealthChecker
from app.application.validator import StartupValidator
from app.core.logger import create_logger
from app.core.settings import Settings
from app.prompt.loader import PromptLoader
from app.prompt.registry import PromptRegistry
from app.prompt.validator import PromptValidator
from app.prompt.renderer import PromptRenderer
from app.prompt.service import PromptService

class ApplicationContainer:
    """
    Composition Root.

    Owns every singleton in the application.
    """

    def __init__(self):
        self._settings = Settings()
        self._logger = create_logger(self._settings)

        self._validator = StartupValidator(self._settings)
        self._banner = StartupBanner(self._settings)
        self._health_checker = HealthChecker(self._settings)

        # It will be injected in the services, not Application below. Application is manage the lifecycle of Application.
        # AI related business logic will live in dedicated services.
        self._ai_provider = AIProviderFactory.create(self._settings)

        self._application = Application(
            logger=self._logger,
            settings=self._settings,
            validator=self._validator,
            banner=self._banner,
            health_checker=self._health_checker
        )
        
        #Future - will keep adding services here
        #self.openai.client

        self._prompt_loader = PromptLoader(Path(self._settings.prompt_directory))
        self._prompt_registry = PromptRegistry(self._prompt_loader)
        self._prompt_validator = PromptValidator()
        self._prompt_renderer = PromptRenderer()
        self._prompt_service = PromptService(
            registry=self._prompt_registry,
            validator=self._prompt_validator,
            renderer=self._prompt_renderer
        )

    @property
    def application(self) -> Application:
        return self._application
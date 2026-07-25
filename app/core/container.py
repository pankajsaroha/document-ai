# heart of the app

from app.application.application import Application
from app.application.banner import StartupBanner
from app.application.health import HealthChecker
from app.application.validator import StartupValidator
from app.core.logger import create_logger
from app.core.settings import Settings

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

        self._application = Application(
            logger=self._logger,
            settings=self._settings,
            validator=self._validator,
            banner=self._banner,
            health_checker=self._health_checker
        )
        
        #Future - will keep adding services here
        #self.openai.client

    @property
    def application(self) -> Application:
        return self._application
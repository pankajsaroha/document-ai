from app.application.banner import StartupBanner
from app.application.health import HealthChecker
from app.application.validator import StartupValidator

class Application:
    """Application entry point."""

    def __init__(
        self,
        logger,
        settings,
        validator: StartupValidator,
        banner: StartupBanner,
        health_checker: HealthChecker
    ) -> None:
        self._logger = logger
        self._settings = settings
        self._validator = validator
        self._banner = banner
        self._health_checker = health_checker

    def start(self):
        self._validator.validate()
        self._banner.print()
        self._health_checker.check()

        self._logger.info(
            "Application started",
            application_name=self._settings.app_name,
            version=self._settings.app_version,
            environment=self._settings.environment
        )

    def stop(self):
        self._logger.info("Application stopped")

    def version(self) -> None:
        print(
            f"{self._settings.app_name} "
            f"{self._settings.app_version}"
        )

    def doctor(self) -> None:  
        self._health_checker.check()
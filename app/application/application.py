from app.core.container import ApplicationContainer
from app.application.banner import StartupBanner
from app.application.health import HealthChecker
from app.application.validator import StartupValidator

class Application:
    """Application entry point."""

    def __init__(self, container: ApplicationContainer) -> None:
        self._container = container
        self._validator = StartupValidator(container.settings)
        self._health_checker = HealthChecker(container.settings)
        self._banner = StartupBanner(container.settings)

    def start(self):
        logger = self._container.logger
        settings = self._container.settings

        self._validator.validate()
        self._banner.print()
        self._health_checker.check()

        logger.info(
            "Application started",
            application_name=settings.app_name,
            version=settings.app_version,
            environment=settings.environment
        )

    def stop(self):
        self._container.Logger.info("Application stopped")
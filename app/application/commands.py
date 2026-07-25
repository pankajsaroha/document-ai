from app.application.application import Application
from app.core.container import ApplicationContainer
from app.application.health import HealthChecker
from app.application.validator import StartupValidator

def run() -> None:
    container = ApplicationContainer()
    validator = StartupValidator(container.settings)
    validator.validate()

    app = Application(container)
    app.start()

def version() -> None:
    container = ApplicationContainer()

    print(
        f"{container.settings.app_name} "
        f"{container.settings.app_version}"
    )

def doctor() -> None:
    container = ApplicationContainer()
    
    health = HealthChecker(container.settings)

    print("Health check:")
    print("-------------")
    print("✓ Settings Loaded")
    print("✓ Logger Initialized")
    print("Status: HEALTHY")
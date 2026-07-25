from app.application.application import Application
from app.core.container import ApplicationContainer
from app.application.health import HealthChecker
from app.application.validator import StartupValidator

def _application():
    return ApplicationContainer().application

def run() -> None:
    _application().start()

def version() -> None:
    _application().version()

def doctor() -> None:
    _application().doctor()
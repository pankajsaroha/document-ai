from app.core.settings import Settings

class StartupValidator:
    
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def validate(self) -> None:
        if not self._settings.app_name:
            raise ValueError("Application name is required")

        if not self._settings.app_version:
            raise ValueError("Application version is required")

        if not self._settings.environment:
            raise ValueError("Environment is required")
from app.core.settings import Settings

class StartupBanner:
    
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def print(self) -> None:
        print("=" * 50)
        print(f"{self._settings.app_name}")
        print(f"Version     : {self._settings.app_version}")
        print(f"Environment : {self._settings.environment}")
        print("=" * 50)
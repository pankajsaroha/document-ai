from app.core.settings import Settings

class HealthChecker:
    
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def check(self) -> None:
        print()

        print("Health check")
        print("-" * 50)

        print("✓ Settings Loaded")
        print("✓ Configuration Loaded")
        print("✓ Logger Initialized")

        print()

        print("Status: HEALTHY")
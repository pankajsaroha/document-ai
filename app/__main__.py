from app.core.container import ApplicationContainer

def main():
    container = ApplicationContainer()
    logger = container.Logger
    settings = container.Settings
    app = Application(container)
    app.start()

    logger.info(
        "Application started",
        application_name=settings.app_name,
        version=settings.app_version,
        environment=settings.environment,
    )

if __name__ == "__main__":
    main()
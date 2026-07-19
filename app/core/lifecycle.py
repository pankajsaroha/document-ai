class Application:

    def __init__(self, container: ApplicationContainer):
        self.container = container

    def start(self) -> None:
        self._container.logger.info("Application started.")
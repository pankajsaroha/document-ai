# heart of the app

from app.core.logger import create_logger
from app.core.settings import Settings

class ApplicationContainer:
    """
    Composition Root.

    Owns every singleton in the application.
    """

    def __init__(self):
        self.Settings = Settings()
        self.Logger = create_logger(self.Settings)
        
# heart of the app

from app.core.logger import create_logger
from app.core.settings import Settings

class ApplicationContainer:
    """
    Composition Root.

    Owns every singleton in the application.
    """

    def __init__(self):
        self.settings = Settings()
        self.logger = create_logger(self.settings)
        
        #Future - will keep adding services here
        #self.openai.client

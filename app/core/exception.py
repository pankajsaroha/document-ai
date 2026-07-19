class DocumentAIException(Exception):
    """Base exception for the application."""

class ConfigurationError(DocumentAIException):
    """Raised when application configuration is invalid."""
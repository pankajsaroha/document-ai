class AIProviderError(Exception):
    """Base AI provider exception."""

class AuthenticationError(AIProviderError):
    """Authentication Failed."""

class RateLimitError(AIProviderError):
    """Rate limit exceeded."""

class ProviderUnavailableError(AIProviderError):
    """Provider unavailable."""
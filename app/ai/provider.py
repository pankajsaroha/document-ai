from abc import ABC, abstractmethod

from app.ai.models import ChatRequest
from app.ai.models import ChatResponse

class AIProvider(ABC):

    @abstractmethod
    def chat(self, request: ChatRequest) -> ChatResponse:
        """Generate a chat completion."""

    @abstractmethod
    def health(self) -> bool:
        """Check provider health."""
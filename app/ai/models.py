from dataclasses import dataclass, field
from enum import Enum
from abc import ABC
from datetime import datetime, timedelta

class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class Provider(str, Enum):
    OPENAI = "openai",
    GEMINI = "gemini",
    ANTHROPIC = "anthropic",
    OLLAMA = "ollama"

# MessagePart is to support Images, PDFs, Audio, Tool calls , Function calls, Structured outputs
# but we are using pass as we need to implement a better strategy to process these types
class MessagePart(ABC):
    pass

@dataclass(slots=True)
class TextPart(MessagePart):
    text: str

@dataclass(slots=True)
class Message:
    role: Role
    parts: list[MessagePart] # we could have used text: str to support string, but we are using MessagePart to support other types

@dataclass(slots=True)
class RequestContext:
    request_id: str
    user_id: str | None = None
    session_id: str | None = None
    tags: dict[str, str] = field(default_factory=dict)

@dataclass(slots=True)
class ChatRequest:
    messages: list[Message]
    context: RequestContext
    requested_at: datetime

    model: str | None = None
    temperature: float = 0.0
    max_tokens: int | None = None
    top_p: float | None = None
    stop: list[str] | None = None
    metadata: dict[str, str] = field(default_factory=dict)
    timeout: timedelta | None = None

@dataclass(slots=True)
class TokenUsage:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

@dataclass(slots=True)
class ChatResponse:
    content: str
    model: str
    provider: Provider

    finish_reason: str | None = None
    response_id: str | None = None
    created_at: int | None = None
    usage: TokenUsage | None = None
    raw_response: object | None = None
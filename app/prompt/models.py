from dataclasses import dataclass, field
from datetime import datetime

@dataclass(slots=True, frozen=True)
class PromptMetadata:
    name: str
    version: str
    description: str | None = None
    created_at: datetime | None = None
    tags: dict[str: str] = field(default_factory=dict)

@dataclass(slots=True, frozen=True)
class Prompt:
    metadata: PromptMetadata
    template: str
    variables: set[str] = field(default_factory=set)
from pathlib import Path
import re

from app.prompt.exceptions import PromptNotFoundError
from app.prompt.exceptions import PromptVersionNotFoundError
from app.prompt.models import Prompt
from app.prompt.models import PromptMetadata

VARIABLE_PATTERN = re.compile(r"{([a-zA-Z_][a-zA-Z0-9_]*)}")

class PromptLoader:
    
    def __init__(self, prompt_directory: Path) -> None:
        self._prompt_directory = prompt_directory

    def load(self, prompt_name: str, version: str | None = None) -> Prompt:
        path = self._resolve_path(prompt_name=prompt_name, version=version)
        template = path.read_text(encoding="utf-8")
        variables = set(
            VARIABLE_PATTERN.findall(template)
        )
        metadata = PromptMetadata(name=prompt_name, version=version or "v1")

        return Prompt(
            metadata=metadata,
            template=template,
            variables=variables
        )

    def _resolve_path(self, prompt_name: str, version: str | None) -> Path:
        
        if version is None:
            path = self._prompt_directory/f"{prompt_name}.md"

            if not path.exists():
                raise PromptNotFoundError(prompt_name)

            return path
        
        path = self._prompt_directory/prompt_name/f"{version}.md"
        
        if not path.exists():
            raise PromptVersionNotFoundError(prompt_name, version)

        return path
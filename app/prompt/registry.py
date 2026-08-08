from app.prompt.loader import PromptLoader
from app.prompt.models import Prompt

#For now it's deliberately thin. Later it can support caching, aliases, default versions, etc.
class PromptRegistry:
    
    def __init__(self, loader: PromptLoader) -> None:
        self._loader = loader

    def get(self, prompt_name: str, version: str | None = None) -> Prompt:
        return self._loader.load(prompt_name=prompt_name, version=version)
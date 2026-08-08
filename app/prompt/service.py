from app.prompt.models import Prompt
from app.prompt.registry import PromptRegistry
from app.prompt.renderer import PromptRenderer
from app.prompt.validator import PromptValidator

class PromptService:

    def __init__(self, registry: PromptRegistry, renderer: PromptRenderer, validator: PromptValidator) -> None:
        self._registry = registry
        self._renderer = renderer
        self._validator = validator

    def render(self, prompt_name: str, version: str | None = None, **variables: str) -> str:
        prompt = self._registry.get(prompt_name=prompt_name, version=version)
        self._validator.validate(prompt, **variables)
        return self._renderer.render(prompt, **variables)
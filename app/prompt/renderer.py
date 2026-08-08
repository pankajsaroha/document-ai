from app.prompt.models import Prompt
from app.prompt.validator import PromptValidator

class PromptRenderer:

    def render(self, prompt: Prompt, **variables: str) -> str:
        return prompt.template.format(**variables)
from app.prompt.exceptions import MissingVariableError, UnknownVariableError
from app.prompt.models import Prompt

class PromptValidator:
    
    def validate(self, prompt: Prompt, **variables: str) -> None:
        self._validate_missing_variables(prompt, variables)
        self._validate_unknown_variables(prompt, variables)

    def _validate_missing_variables(self, prompt: Prompt, variables: dict[str, str]) -> None:
        missing_variables = prompt.variables - set(variables.keys())

        if missing_variables:
            raise MissingVariableError(next(iter(missing_variables)))

    def _validate_unknown_variables(self, prompt: Prompt, variables: dict[str, str]) -> None:
        unknown_variables = set(variables.keys()) - prompt.variables

        if unknown_variables:
            raise UnknownVariableError(next(iter(unknown_variables)))
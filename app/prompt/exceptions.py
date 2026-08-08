class PromptError(Exception):
    pass

class PromptNotFoundError(PromptError):

    def __init__(self, name: str):
        super().__init__(f"Prompt '{name}' was not found.")

class PromptVersionNotFoundError(PromptError):
    def __init__(self, name: str, version: str):
        super().__init__(f"Prompt '{name}' version '{version}' was not found.")

class PromptValidationError(PromptError):
    pass

class MissingVariableError(PromptValidationError):
    def __init__(self, variable: str):
        super().__init__(f"Missing variable: '{variable}'")

class UnknownVariableError(PromptValidationError):
    def __init__(self, variable: str):
        super().__init__(f"Unknown variable: '{variable}'")
import pytest

from app.prompt.validator import PromptValidator
from app.prompt.models import Prompt, PromptMetadata
from app.prompt.exceptions import MissingVariableError, UnknownVariableError

def test_validate_success():
    prompt = Prompt(
        metadata = PromptMetadata(
            name="rewrite",
            version="v1"
        ),
        template="Hello {name}",
        variables={"name"},
    )

    validator = PromptValidator()

    validator.validate(prompt, name="Pankaj")

def test_missing_variable():
    prompt = Prompt(
        metadata = PromptMetadata(
            name="rewrite",
            version="v1",
        ),
        template="Hello {name}",
        variables={"name"}
    )

    validator = PromptValidator()

    with pytest.raises(MissingVariableError):
        validator.validate(prompt)

def test_unknown_variable():
    prompt = Prompt(
        metadata = PromptMetadata(
            name="rewrite",
            version="v1",
        ),
        template="Hello {name}",
        variables={"name"},
    )

    validator = PromptValidator()

    with pytest.raises(UnknownVariableError):
        validator.validate(prompt, name="Pankaj", age="26")
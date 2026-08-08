import pytest

from app.prompt.exceptions import (
    PromptNotFoundError
)

def test_prompt_not_found():
    with pytest.raises(PromptNotFoundError):
        raise PromptNotFoundError("chat")
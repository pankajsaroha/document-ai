import pytest

from unittest.mock import MagicMock

from app.prompt.models import Prompt
from app.prompt.registry import PromptRegistry

def test_get_prompt():
    loader = MagicMock()
    prompt = Prompt(metadata=MagicMock(), template="Hello {name}", variables={"name"})
    loader.load.return_value = prompt

    registry = PromptRegistry(loader)
    result = registry.get(prompt_name="chat", version="v1")

    assert result is prompt

    loader.load.assert_called_once_with(prompt_name="chat", version="v1")
import pytest

from unittest.mock import MagicMock

from app.prompt.models import Prompt
from app.prompt.service import PromptService

def test_render_prompt():
    registry = MagicMock()
    validator = MagicMock()
    renderer = MagicMock()

    prompt = Prompt(metadata=MagicMock(), template="Hello {name}", variables={"name"})

    registry.get.return_value = prompt
    renderer.render.return_value = "Hello Pankaj"

    service = PromptService(registry=registry, validator=validator, renderer=renderer)

    result = service.render(prompt_name="chat", user_name="Pankaj")

    assert result == "Hello Pankaj"

    registry.get.assert_called_once_with(prompt_name="chat", version=None)
    validator.validate.assert_called_once_with(prompt, user_name="Pankaj")
    renderer.render.assert_called_once_with(prompt, user_name="Pankaj")
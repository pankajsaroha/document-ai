import pytest

from pathlib import Path

from app.prompt.loader import PromptLoader
from app.prompt.registry import PromptRegistry
from app.prompt.renderer import PromptRenderer
from app.prompt.service import PromptService
from app.prompt.validator import PromptValidator

def test_prompt_system_end_to_end():
    prompt_directory = (Path(__file__).parents[2]/"resources"/"prompts")

    loader = PromptLoader(prompt_directory)
    registry = PromptRegistry(loader)
    validator = PromptValidator()
    renderer = PromptRenderer()

    service = PromptService(registry=registry, validator=validator, renderer=renderer)

    result = service.render(prompt_name="summarize", language="english", text="This document contains financial results.")

    assert result == (
        "You are a document summarization assistant.\n\n"
        "Summarize the following document in english.\n\n"
        "Document:\n\n"
        "This document contains financial results."
    )
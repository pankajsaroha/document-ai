import pytest

from pathlib import Path
from app.prompt.loader import PromptLoader
from app.prompt.exceptions import PromptNotFoundError, PromptVersionNotFoundError

from app.core.settings import Settings

# happy path
def test_load_prompt():

    loader = PromptLoader(Path("tests/resources/prompts"))
    prompt = loader.load("rewrite")

    assert prompt.metadata.name == "rewrite"
    assert prompt.variables == {
        "tone",
        "text",
    }

# prompt not found
def test_prompt_not_found():
    loader = PromptLoader(Path("tests/resources/prompts"))
    
    with pytest.raises(PromptNotFoundError):
        loader.load("unknown")

# prompt version not found
def test_version_not_found():
    loader = PromptLoader(Path("tests/resources/prompts"))

    with pytest.raises(PromptVersionNotFoundError):
        loader.load(prompt_name="rewrite", version="v99")
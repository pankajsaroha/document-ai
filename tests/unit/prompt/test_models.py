from app.prompt.models import Prompt, PromptMetadata

def test_prompt():
    prompt = Prompt(
        metadata = PromptMetadata(
            name = "chat",
            version = "v1"
        ),
        template = "Hello {name}",
        variables = {"name"}
    )

    assert prompt.metadata.name == "chat"
    assert prompt.metadata.version == "v1"
    assert prompt.variables == {"name"}
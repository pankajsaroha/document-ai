# RUN_SMOKE_TESTS=1 uv run pytest tests/smoke

from app.ai.factory import AIProviderFactory
from app.ai.models import ChatRequest, Message, RequestContext, Role, TextPart

from datetime import datetime

from app.core.settings import Settings

def test_openai_smoke():
    provider = AIProviderFactory.create(Settings())

    response = provider.chat(
        ChatRequest(
            model="gpt-5",
            requested_at=datetime.now(),
            context=RequestContext(
                request_id="smoke-1",
                user_id=None,
                session_id=None,
            ),
            messages=[
                Message(
                    role=Role.USER,
                    parts=[
                        TextPart(
                            text="Say hello in one sentence."
                        )
                    ]
                )
            ]
        )
    )

    assert response.content
    assert len(response.content) > 0
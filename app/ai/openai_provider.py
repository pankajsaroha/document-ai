from openai import OpenAI
from openai import AuthenticationError as OpenAIAuthenticationError
from openai import RateLimitError as OpenAIRateLimitError
from openai import APIConnectionError
from openai import APITimeoutError

from app.ai.exceptions import (
    AuthenticationError,
    ProviderUnavailableError,
    RateLimitError
)

from app.ai.provider import AIProvider
from app.core.settings import Settings

from app.ai.models import ChatRequest, ChatResponse, MessagePart, TextPart, TokenUsage, Provider

class OpenAIProvider(AIProvider):

    def __init__(
        self,
        settings: Settings,
        client: OpenAI
    ):
        self._settings = settings
        self._client = client

    def chat(self, request: ChatRequest) -> ChatResponse:
        try:
            messages = self._build_messages(request)
            response = self._create_chat_completion(request, messages)

            return self._to_chat_response(response)

        except OpenAIAuthenticationError as ex:
            raise AuthenticationError(str(ex)) from ex

        except OpenAIRateLimitError as ex:
            raise RateLimitError(str(ex)) from ex

        except (APIConnectionError, APITimeoutError) as ex:
            raise ProviderUnavailableError(str(ex)) from ex

    def _build_messages(
        self,
        request: ChatRequest
    ) -> list[dict]:
        return [
            {
                "role": message.role.value,
                "content": self._build_parts(message.parts)
            }
            for message in request.messages
        ]

    def _build_parts(self, parts: list[MessagePart]) -> list[dict]:
        result = []

        for part in parts:
            if isinstance(part, TextPart):
                result.append(
                    {
                        "type": "text",
                        "text": part.text
                    }
                )
            else:
                raise ValueError(f"Unsupported message part: {type(part)}")

        return result

    def _to_chat_response(
        self,
        response,
    ) -> ChatResponse:
        choice = response.choices[0]
        
        usage = None
        if response.usage:
            usage = TokenUsage(
                prompt_tokens = response.usage.prompt_tokens,
                completion_tokens = response.usage.completion_tokens,
                total_tokens = response.usage.total_tokens,
            )

        return ChatResponse(
            content = choice.message.content or "",
            model = response.model,
            provider = Provider.OPENAI,
            response_id = response.id,
            created_at = response.created,
            finish_reason = choice.finish_reason,
            usage = usage,
            raw_response = response,
        )

    def _create_chat_completion(
        self,
        request: ChatRequest,
        messages: list[dict[str, str]]
    ): 
        return self._client.chat.completions.create(
                model = request.model or self._settings.openai_model,
                messages = messages,
                temperature = request.temperature,
                max_completion_tokens = request.max_tokens,
            )

    def health(self) -> bool:
        try:
            self._client.models.list()
            return True

        except (
            OpenAIAuthenticationError,
            OpenAIRateLimitError,
            APIConnectionError,
            APITimeoutError
        ):
            return False
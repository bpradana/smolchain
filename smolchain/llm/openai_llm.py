import os
from typing import Generator, Optional, Self

from openai import OpenAI

from smolchain.chain import RunnableStream
from smolchain.llm.base import BaseLLM
from smolchain.message import AssistantMessage, MessageTemplate


class OpenAILLM(BaseLLM):
    provider = "openai"

    def __init__(
        self,
        model_name: str,
        temperature: float,
        api_key: Optional[str] = None,
    ) -> None:
        super().__init__(model_name, temperature, api_key)
        self.client = OpenAI(
            api_key=(
                os.getenv("OPENAI_API_KEY") if self.api_key is None else self.api_key
            )
        )

    def __call__(self, input: MessageTemplate) -> Self:
        self.messages = input.invoke(self.provider)
        return self

    def invoke(self) -> AssistantMessage:
        chat_completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,  # type: ignore
            temperature=self.temperature,
        )
        return AssistantMessage(chat_completion.choices[0].message.content or "")

    def stream(self) -> Generator[AssistantMessage, None, None]:
        stream = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,  # type: ignore
            temperature=self.temperature,
            stream=True,
        )

        for chunk in stream:
            yield AssistantMessage(chunk.choices[0].delta.content or "")

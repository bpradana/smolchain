from abc import abstractmethod
from typing import Any, Dict, Generator, Optional, Self

from smolchain.chain import Runnable, RunnableStream
from smolchain.message import AssistantMessage


class BaseLLM(Runnable, RunnableStream):
    provider = None

    def __init__(
        self,
        model_name: str,
        temperature: float,
        api_key: Optional[str] = None,
    ) -> None:
        self.model_name = model_name
        self.temperature = temperature
        self.api_key = api_key

    @abstractmethod
    def __call__(self, input: Dict[str, str]) -> Self:
        pass

    @abstractmethod
    def invoke(self) -> AssistantMessage:
        pass

    @abstractmethod
    def stream(self) -> Generator[AssistantMessage, None, None]:
        pass

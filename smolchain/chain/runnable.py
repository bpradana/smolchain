from abc import ABC, abstractmethod
from typing import Any, Generator


class Runnable(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def invoke(self) -> Any:
        pass


class RunnableStream(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def stream(self) -> Generator[Any, None, None]:
        pass

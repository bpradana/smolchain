from typing import Any, Generator, Union

from smolchain.chain import Runnable, RunnableStream
from smolchain.message import AssistantMessage


class StringParser(Runnable, RunnableStream):
    def __init__(
        self,
        input: Union[Runnable, RunnableStream],
    ) -> None:
        self.input = input

    def invoke(self) -> str:
        assert isinstance(self.input, Runnable), "Input must be a Runnable."
        output = self.input.invoke()
        return output.content

    def stream(self) -> Generator[str, None, None]:
        assert isinstance(self.input, RunnableStream), "Input must be a Generator."
        for message in self.input.stream():
            yield message.content

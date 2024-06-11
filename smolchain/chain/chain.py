from functools import reduce
from typing import Any, Self

from smolchain.chain.runnable import Runnable, RunnableStream


class Input(Runnable, RunnableStream):
    def __init__(self, *args) -> None:
        self.inputs = args
        self.functions = []

    def __or__(self, other) -> Self:
        self.functions.append(other)
        return self

    def __call__(self) -> Any:
        return reduce(
            lambda x, function: (
                function(x)
                if not (isinstance(x, list) or isinstance(x, tuple))
                else function(*x)
            ),
            self.functions,
            self.inputs,
        )

    def invoke(self) -> Any:
        pass

    def stream(self) -> Any:
        pass

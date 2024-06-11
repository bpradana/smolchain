from typing import Dict, Iterable, List

from smolchain.message.base import BaseMessage


class MessageTemplate:
    def __init__(self, messages: Iterable[BaseMessage]) -> None:
        self.messages = messages
        self.messages_string = "\n".join(str(message) for message in self.messages)

    def __call__(self, **kwargs) -> str:
        return self.messages_string.format(**kwargs)

    def __str__(self) -> str:
        return self.messages_string

    def invoke(self, provider: str) -> Iterable[Dict[str, str]]:
        return [message.invoke(provider) for message in self.messages]

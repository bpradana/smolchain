from smolchain.message.base import BaseMessage


class AssistantMessage(BaseMessage):
    def __init__(self, content) -> None:
        super().__init__(content)

from smolchain.message.base import BaseMessage


class SystemMessage(BaseMessage):
    def __init__(self, content) -> None:
        super().__init__(content)

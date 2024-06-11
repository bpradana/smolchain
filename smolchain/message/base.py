from typing import Dict, Optional

from smolchain.chain import Runnable


class BaseMessage(Runnable):
    def __init__(self, content: Optional[str]) -> None:
        self.content = content if content else ""
        self.role = self.__class__.__name__.replace("Message", "")

    def __str__(self) -> str:
        return f"{self.role}: {self.content}"

    def __call__(self, **kwargs) -> str:
        return self.content.format(**kwargs)

    def invoke(self, provider: str) -> Dict[str, str]:
        invocations = {
            "openai": self._invoke_openai,
        }
        return invocations[provider]()

    def _invoke_openai(self) -> Dict[str, str]:
        return {
            "role": self.role.lower(),
            "content": self.content,
        }

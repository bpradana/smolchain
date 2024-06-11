from dotenv import load_dotenv

from smolchain.chain import Input
from smolchain.llm import OpenAILLM
from smolchain.message import (
    AssistantMessage,
    MessageTemplate,
    SystemMessage,
    UserMessage,
)
from smolchain.parser import StringParser

if __name__ == "__main__":
    load_dotenv()

    message_template = MessageTemplate(
        [
            SystemMessage("You are a helpful assistant."),
            AssistantMessage("Hi, how can i help you?"),
            UserMessage("Explain python to me."),
        ]
    )

    llm = OpenAILLM(
        model_name="gpt-3.5-turbo",
        temperature=0.7,
    )

    chain = (Input(message_template) | llm | StringParser)()
    output = chain.invoke()
    print(output)

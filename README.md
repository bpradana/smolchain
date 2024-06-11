# SmolChain
Smol replacement for LangChain

## Preface
LangChain, as we all know, is touted as a powerful tool for developing large language model applications. However, it is not the most efficient tool for small projects. In reality, LangChain isn't a library; it's a collection of demos held together by duct tape, f-strings, and prayers. This is where SmolChain comes in. SmolChain is a lightweight, easy-to-use, and efficient alternative to LangChain. It's designed for small projects and is perfect for beginners who don't want to wrestle with the monstrosity of LangChain.

## Installation
Currently, SmolChain is not a pip package yet, but you can clone the repository and play around with it. To clone the repository, run the following command:
1. Clone the repository
```bash
git clone https://github.com/bpradana/smolchain.git
```
2. Install the dependencies
```bash
pip install -r requirements.txt
```
3. Run the example
```bash
python main.py
```

## Usage
SmolChain is designed to be beginner-friendly. It's easy to use and doesn't require a lot of boilerplate code. Here's a simple example of how to use SmolChain:

```python
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
```

I know this example is very similar to LangChain, but the beauty lies in the source code. SmolChain is designed to be beginner-friendly, and the source code is easy to understand. You can easily modify the source code to suit your needs. It's not bloated with unnecessary features, and it's easy to extend unlike LangChain.

## Contributing
SmolChain is an open-source project, and we welcome contributions from the community. If you have any ideas or suggestions, feel free to open an issue or submit a pull request.

## License
SmolChain is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

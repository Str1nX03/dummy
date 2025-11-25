from langchain_ollama.chat_models import ChatOllama

def ollama_llm():

    llm = ChatOllama(
        model = "gemma3:1b",
        temperature = 0.1
    )

    return llm
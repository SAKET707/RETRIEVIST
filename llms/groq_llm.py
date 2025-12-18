import os
from langchain_groq import ChatGroq
from config.settings import LLM_MODEL_NAME, LLM_TEMPERATURE


def get_llm():
    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model=LLM_MODEL_NAME,
        temperature=LLM_TEMPERATURE,
    )


def get_llm_with_tools(tools):
    llm = get_llm()
    return llm.bind_tools(tools)

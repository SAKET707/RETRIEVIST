from typing import List, Optional
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage

from rag.vectorstore import get_retriever
from llms.groq_llm import get_llm
from config.prompts import RAG_PROMPT, SYSTEM_PROMPT
from config.settings import TOP_K
from memory.chat_history import ChatHistory

from utils.helpers import format_docs_as_context


def run_rag(query: str, history: Optional[ChatHistory] = None) -> str:
    retriever = get_retriever(top_k=TOP_K)
    docs = retriever.invoke(query)

    if not docs:
        return "I don't know based on the provided context."
    context = format_docs_as_context(docs)


    rag_prompt = RAG_PROMPT.format(
        context=context,
        question=query,
    )

    messages = []

    if history:
        messages.extend(history.get_messages())

    messages.append(SystemMessage(content=SYSTEM_PROMPT))
    messages.append(HumanMessage(content=rag_prompt))

    llm = get_llm()
    response = llm.invoke(messages)

    return response.content

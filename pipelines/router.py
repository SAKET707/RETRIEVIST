from langchain_core.messages import SystemMessage, HumanMessage
from rag.rag_pipeline import run_rag
from pipelines.agent_pipeline import run_agent
from llms.groq_llm import get_llm
from config.prompts import GENERAL_PROMPT


def _needs_tools(query: str) -> bool:
    tool_keywords = [
        "latest",
        "current",
        "news",
        "price",
        "calculate",
        "fetch",
        "lookup",
        "search",
    ]
    q = query.lower()
    return any(k in q for k in tool_keywords)


def _looks_like_rag(query: str) -> bool:
    rag_keywords = [
        "document",
        "pdf",
        "according to",
        "based on",
        "context",
        "from the file",
    ]
    q = query.lower()
    return any(k in q for k in rag_keywords)



def run_general(query: str, history=None) -> str:
    llm = get_llm()

    messages = []

    if history:
        messages.extend(history.get_messages())

    messages.append(
        HumanMessage(
            content=GENERAL_PROMPT.format(question=query)
        )
    )

    return llm.invoke(messages).content


def route_query(query: str, history=None) -> str:
    if _needs_tools(query):
        return run_agent(query, history)

    if _looks_like_rag(query):
        return run_rag(query, history)

    return run_general(query, history)


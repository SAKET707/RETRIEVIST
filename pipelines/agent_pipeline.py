from typing import Optional
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from llms.groq_llm import get_llm
from config.prompts import AGENT_PROMPT
from memory.chat_history import ChatHistory

from tools.calculator import calculate
from tools.wiki_tool import wikipedia_search
from tools.arxiv_tool import arxiv_search


def run_agent(query: str, history: Optional[ChatHistory] = None) -> str:
    tools = [calculate, wikipedia_search, arxiv_search]
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", AGENT_PROMPT),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    agent = create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,
    )

    result = executor.invoke(
        {
            "input": query,
            "chat_history": history.get_messages() if history else [],
        }
    )

    return result["output"]

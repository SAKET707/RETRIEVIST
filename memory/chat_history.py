from typing import List
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    BaseMessage,
)

from config.settings import MAX_HISTORY_MESSAGES


class ChatHistory:
    def __init__(self):
        self.messages: List[BaseMessage] = []

    def _trim(self):
        """
        Keep only the most recent MAX_HISTORY_MESSAGES.
        """
        if len(self.messages) > MAX_HISTORY_MESSAGES:
            self.messages = self.messages[-MAX_HISTORY_MESSAGES:]

    def add_user_message(self, content: str):
        self.messages.append(HumanMessage(content=content))
        self._trim()

    def add_ai_message(self, content: str):
        self.messages.append(AIMessage(content=content))
        self._trim()

    def get_messages(self) -> List[BaseMessage]:
        """
        Returns trimmed chat history.
        """
        return self.messages

    def clear(self):
        self.messages = []

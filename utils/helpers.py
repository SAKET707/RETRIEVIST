from typing import List
from langchain_core.documents import Document


def format_docs_as_context(docs: List[Document]) -> str:
    """
    Converts a list of Documents into a single context string.
    Used by RAG pipelines.
    """
    return "\n\n".join(doc.page_content for doc in docs)


def safe_lower(text: str) -> str:
    """
    Safely lowercase a string.
    """
    return text.lower().strip() if text else ""


def truncate_text(text: str, max_length: int = 2000) -> str:
    """
    Truncate text to a maximum length.
    Useful to avoid token overflow.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

from typing import List
from langchain_core.documents import Document

from rag.loaders import load_pdf, load_text, load_web
from rag.splitter import split_documents
from rag.vectorstore import add_documents


def _ingest_documents(documents: List[Document]) -> int:
    """
    Common ingestion pipeline:
    load → split → embed → store
    Returns number of chunks stored.
    """
    if not documents:
        return 0

    chunks = split_documents(documents)
    if not chunks:
        return 0

    add_documents(chunks)
    return len(chunks)


def ingest_pdf(file_path: str) -> int:
    """
    Ingest a PDF file into the vector store.
    """
    documents = load_pdf(file_path)
    return _ingest_documents(documents)


def ingest_text(file_path: str) -> int:
    """
    Ingest a text file into the vector store.
    """
    documents = load_text(file_path)
    return _ingest_documents(documents)


def ingest_web(url: str) -> int:
    """
    Ingest a web page into the vector store.
    """
    documents = load_web(url)
    return _ingest_documents(documents)

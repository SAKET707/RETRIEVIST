from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
)


def load_pdf(path: str) -> List[Document]:
    loader = PyPDFLoader(path)
    documents = loader.load()
    cleaned_docs = [
        doc for doc in documents
        if doc.page_content and doc.page_content.strip()
    ]

    return cleaned_docs


def load_text(path: str) -> List[Document]:
    loader = TextLoader(
        path,
        encoding="utf-8",
        autodetect_encoding=True,
    )
    return loader.load()


def load_web(url: str) -> List[Document]:
    loader = WebBaseLoader(url)
    return loader.load()

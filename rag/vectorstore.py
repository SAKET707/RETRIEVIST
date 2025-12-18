import os
from typing import List
from pinecone import Pinecone
from langchain_core.documents import Document
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from llms.embeddings import get_embeddings
from config.settings import PINECONE_INDEX_NAME
from config.settings import TOP_K


def _get_pinecone_index():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    return pc.Index(PINECONE_INDEX_NAME)



def get_vectorstore():
    index = _get_pinecone_index()
    embeddings = get_embeddings()

    return LangchainPinecone(
        index=index,
        embedding=embeddings,
        text_key="page_content",
    )


def add_documents(documents: List[Document]):
    vectorstore = get_vectorstore()
    vectorstore.add_documents(documents)



def get_retriever(top_k: int = TOP_K):
    vectorstore = get_vectorstore()
    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": top_k},
    )

def clear_vectorstore():
    """
    Safely clears all vectors from the default namespace.
    If the namespace does not exist yet, do nothing.
    """
    index = _get_pinecone_index()

    try:
        index.delete(delete_all=True, namespace="")
    except Exception as e:
        msg = str(e).lower()
        if "namespace not found" in msg or "404" in msg:
            return
        raise


from langchain_core.tools import tool
from langchain_community.utilities import ArxivAPIWrapper

arxiv_api = ArxivAPIWrapper(
    top_k_results=3,
    doc_content_chars_max=1500,
)


@tool
def arxiv_search(query: str) -> str:
    """
    Fetch raw arXiv paper titles and abstracts for a given research query.
    The calling model should summarize or extract key points.
    """
    return arxiv_api.run(query)

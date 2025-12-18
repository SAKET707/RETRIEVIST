from langchain_core.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper

wiki_api = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=1200,
    load_all_available_meta=False,
)


@tool
def wikipedia_search(query: str) -> str:
    """
    Fetch raw Wikipedia content for a given topic.
    The calling model should summarize or control length.
    """
    return wiki_api.run(query)


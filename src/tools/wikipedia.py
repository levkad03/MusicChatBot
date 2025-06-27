from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


def get_wikipedia_tool():
    wiki_api = WikipediaAPIWrapper(
        lang="en", top_k_results=1, doc_content_chars_max=2000
    )

    return WikipediaQueryRun(api_wrapper=wiki_api)

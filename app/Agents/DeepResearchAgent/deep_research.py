from langchain_community.utilities import SerpAPIWrapper
from langchain_core.tools import Tool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchResults
# from langchain.document_loaders import WebBaseLoader 
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain_community.document_loaders import WebBaseLoader
import os
from bs4 import BeautifulSoup

# # initialize SerpAPI search wrapper
search = SerpAPIWrapper(
    serpapi_api_key=os.getenv("SERP_API_KEY"),
)
# wrap as a Tool for agents
search_tool = Tool(
    name="serpapi_search",
    description="Use this to search the web via SerpAPI",
    func=search.run
)
wrapper = DuckDuckGoSearchAPIWrapper()
web_search = DuckDuckGoSearchResults(
    api_wrapper=wrapper,
    results_separator="\n",
    max_results=10,
    return_direct_results=True,
    output_format= 'string'
    )

result = web_search.run("Current trends in AI research")
print(result)



def websearch_and_load(query: str):
    """
    Perform web search and load result URLs into documents.
    """
    search_results = web_search.run(query)  # returns list[dict]
    if not isinstance(search_results, list):
        return []
    
    urls = [r["link"] for r in search_results if "link" in r]
    if not urls:
        return []
    
    # Load web content
    loader = WebBaseLoader(urls)
    raw_docs = loader.load()
    
    # Clean HTML using BeautifulSoup
    transformer = BeautifulSoupTransformer()
    docs = transformer.transform_documents(raw_docs)
    
    return docs



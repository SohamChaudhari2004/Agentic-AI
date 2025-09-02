from langchain_mistralai import ChatMistralAI
from langchain.indexes import VectorstoreIndexCreator

import os

llm = ChatMistralAI(
    api_key= os.getenv("MISTRAL_API_KEY"),
    model_name="mistral-large-latest",
    temperature=0.7,
)


def build_index(docs):
    """
    Build an index from the provided documents.
    
    Args:
        docs (list): List of documents to index.

    Returns:
        VectorstoreIndexCreator: An index created from the documents.
    """
    index = VectorstoreIndexCreator().from_documents(docs)
    return index

def answer_with_rag(index, query):
    """
    Answer a query using the provided index.
    
    Args:
        index (VectorstoreIndexCreator): The index to use for answering.
        query (str): The query to answer.

    Returns:
        str: The answer to the query.
    """
    query_engine = index.as_query_engine(
        similarity_top_k=5,
        llm=llm
    )
    response = query_engine.query(query)
    return response.response
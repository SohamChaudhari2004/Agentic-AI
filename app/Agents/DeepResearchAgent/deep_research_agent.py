from langchain_mistralai import ChatMistralAI
from langgraph.prebuilt import create_react_agent
from deep_research import websearch_and_load
from rag import build_index, answer_with_rag
from langchain_core.tools import Tool

model = ChatMistralAI(
    model_name="mistral-large-latest",
    temperature=0.7,
)

def deep_research_tool_fn(input: str):
    """
    Create a deep research agent using the Mistral model.
    
    Returns:
        Agent: A react agent configured for deep research tasks.
    """
    docs = websearch_and_load(input)
    print(f"Tool called with query: {input}")  # Debug
    if not docs:
        return {"answer": "No relevant documents found.", "docs": []}
    index = build_index(docs)
    answer = answer_with_rag(index, input)
    return {"answer": answer, "docs": [doc.page_content[:300] for doc in docs]}

deep_research_tool = Tool(
    name="deep_research_tool",
    description="Use this tool to perform deep research on a given query. It searches the web, loads documents, and answers questions based on the latest research trends.",
    func=deep_research_tool_fn,
)

websearch_agent = create_react_agent(
    model = model,
    tools = [deep_research_tool],
    name = "deep_research_agent",
    prompt=(
        "You are a deep research agent. Your task is to perform web searches and answer questions based on the latest research trends. "
        "Use the provided tools to search the web and retrieve relevant information. "
        "Respond with the most accurate and up-to-date information available."
        "Keep your responses detailed and focused on the query at hand."
        "If you cannot find relevant information, state that clearly."
        "Use the websearch_and_load function to perform searches and load documents."
        "Use the build_index function to create an index from the documents."
    )
)
    

response = websearch_agent.invoke({'input' : "What are the latest trends in AI research?"})  # Example query to invoke the agent

print(response)  # Print the response from the agent
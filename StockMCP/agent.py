import asyncio
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()


async def create_mcp_agent_executor():
    # Initialize Groq LLM
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="openai/gpt-oss-120b",
        temperature=0,
    )

    # MCP client
    mcp_client = MultiServerMCPClient(
        {
            "yfinanceserver": {
                "transport": "stdio",
                "command": "uv",
                "args": ["run", "D:\\AIML\\Research\\StockMCP\\server.py"],
            }
        }
    )

    # Get MCP tools
    tools = await mcp_client.get_tools()

    # Prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a financial assistant. Use tools when needed to answer stock-related questions accurately.",
            ),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )
    
    # Create agent
    agent = create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

    # Wrap agent in executor (THIS IS REQUIRED)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
    )

    return agent_executor


async def main():   
    agent_executor = await create_mcp_agent_executor()

    while True:
        user_input = await asyncio.to_thread(input, "\nYou: ")

        if user_input.lower() in {"exit", "quit", "q"}:
            break

        response = await agent_executor.ainvoke(
            {"input": user_input}
        )

        print(f"\nAgent: {response['output']}")


if __name__ == "__main__":
    asyncio.run(main())

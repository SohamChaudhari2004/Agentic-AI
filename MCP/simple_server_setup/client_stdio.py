import asyncio
from xmlrpc import client
import nest_asyncio
from mcp import StdioServerParameters, ClientSession
from mcp.client.stdio import stdio_client

nest_asyncio.apply()

async def main():
    server_params = StdioServerParameters(
        command = 'python',
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tool_res = await session.list_tools()

            print("avaulable tools:")
            for tool in tool_res.tools:
                print(f"- {tool.name}: {tool.description}")

            res = await session.call_tool("add", {"a": 5, "b": 10})
            print(f"add(5, 10) = {res.content}")

if __name__ == "__main__":
    asyncio.run(main())
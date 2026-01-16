from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv(".env") 

mcp = FastMCP(
    name='calculator',
    host='0.0.0.0',
    port=8050
)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    transport = "stdio"
    if transport == "stdio":
        print("Starting server with stdio transport")
        mcp.run(transport="stdio")

    elif transport == "sse":
        print("Starting server with sse transport")
        mcp.run(transport="sse")
    else:
        raise ValueError("Invalid transport")
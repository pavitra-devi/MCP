from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
load_dotenv()

mcp=FastMCP(
    name="calculator",
    host="localhost",#when running the server remotely (SSE transport)
    port=8050, #when running the server remotely (SSE transport)
)

@mcp.tool()
def add(a:int,b:int)->int:
    """
    Adds two numbers together.
    """
    return a + b


@mcp.tool()
def subtract(a:int,b:int)->int:
    """
    Subtracts the second number from the first.
    """
    return a - b

@mcp.tool()
def multiply(a:int,b:int)->int:
    """
    Multiplies two numbers together.
    """
    return a * b

@mcp.tool()
def divide(a:int,b:int)->float:
    """
    Divides the first number by the second.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    transport="stdio"
    if(transport=="stdio"):
        print("Starting MCP server on stdio...")
        mcp.run(transport="stdio")
    elif(transport=="sse"):
        print("Starting MCP server on SSE...")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unsupported transport type. Use 'stdio' or 'sse'.{transport}")
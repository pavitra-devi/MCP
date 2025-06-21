import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

nest_asyncio.apply()  # Needed to run interactive python

"""
Make sure:
1. The server is running before running this script.
2. The server is configured to use SSE transport.
3. The server is listening on port 8050.

To run the server:
uv run server.py
"""


async def main():
    #connect to server
    async with sse_client("http://localhost:8050/sse") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            #initialize the session
            await session.initialize()

            tool_result = await session.list_tools()
            print("Available tools:", tool_result)

            for tool in tool_result.tools:
                print(f"  - {tool.name}: {tool.description} ")
            
            #calling multiplication tool
            result= await session.call_tool("multiply", arguments={"a": 5, "b": 3})
            print("Result of multiplication:", result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
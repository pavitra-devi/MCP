import asyncio
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    #Define server parameters
    server_params= StdioServerParameters(
        name="calculator",
        command='python', #commnad to run the server python sdk
        args=['server.py'],  #arguments to pass to the server script
    )

    #connect to the server
    async with stdio_client(server_params) as (read_stream,write_stream):
        async with ClientSession(read_stream,write_stream) as session:
            #initialize the session
            await session.initialize()

            tool_result=await session.list_tools()
            print("Available tools:", tool_result)
            
            #we can access the tools from tools key
            for tool in tool_result.tools:
                print(f"  - {tool.name}: {tool.description}")
            

            #calling the tool:
            result = await session.call_tool("add",arguments={"a": 5, "b": 3})
            # print(f"Result of add: {result}")
            print("result of addition :",result.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())
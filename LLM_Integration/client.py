from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
import json
import os

load_dotenv("../.env")

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm=init_chat_model(model_provider="google_genai",model="gemini-2.0-flash-001",)

#helper function for calling open ai
def call_llm(user_query, tools):
    token=os.environ["GITHUB_TOKEN"]
    endpoint="https://models.inference.ai.azure.com"
    model_name="gpt-4o"
    client= ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
    )

    print("Calling LLM")
    response = client.complete(
        messages=[
            {
                "role":"system",
                "content":" you are a helpful assistant"
            
            },
            {
                "role":"user",
                "content": user_query
            }
        ],
        model=model_name,
        tools=tools,
        tool_choice="auto",
    )
    response_messages = response.choices[0].message
    print("LLM response:", response_messages)
    functions_to_call=[]
    if response_messages.tool_calls:
        for tool_call in response_messages.tool_calls:
            name= tool_call.function.name
            args= tool_call.function.arguments
            functions_to_call.append({
                "name": name,
                "arguments": json.loads(args)
            })
    return functions_to_call


server_params=StdioServerParameters(
    name="RAG_tools",
    command='python',  # Command to run the server Python SDK
    args=['server.py'],  # Arguments to pass to the server script
)

def convert_to_llm_tool(tool):
    tool_schema={
        "type":"function",
        "function":{
            "name":tool.name,
            "description":tool.description,
            "type":"function",
            "parameters":{
                "type":"object",
                "properties":tool.inputSchema['properties']
                
            }
        }
    }
    return tool_schema

async def run():
    #connect to server
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream,write_stream) as session:
            await session.initialize()
            functions=[]
            tool_result = await session.list_tools()
            for tool in tool_result.tools:
                print(f"Tool: {tool.name}, Description: {tool.description}")
                functions.append(convert_to_llm_tool(tool))
            print("tool_schema for llm:", functions)

            #call the LLM
            user_query = "How do I submit an expense report?"
            functions_to_call = call_llm(user_query, functions)
            for f in functions_to_call:
                if f['name'] == "get_context_for_llm":
                    print("Calling get_context_for_llm tool with query:", f["arguments"]["query"])
                    result= await session.call_tool(
                        f["name"],
                        arguments=f["arguments"]
                    )
                    context = result.content[0].text
                    GENERATE_PROMPT = (
                        "You are an assistant for question-answering tasks. "
                        "Use the following pieces of retrieved context to answer the question. "
                        "If you don't know the answer, just say that you don't know. "
                        "Use five sentences maximum and keep the answer concise.\n"
                        "Question: {user_query} \n"
                        "Context: {context}\n"
                    )
                    prompt = GENERATE_PROMPT.format(
                        user_query=user_query,
                        context=context
                    )
                    final_response = llm.invoke([{"role":"user","content":prompt}])
                    print("Final response from LLM:", final_response.content)
                else:
                    result=await session.call_tool(
                        f["name"],
                        arguments=f["arguments"]
                    )
                    print(f"Result of {f['name']}:", result.content[0].text)


if __name__ == "__main__":
    import asyncio
    asyncio.run(run())



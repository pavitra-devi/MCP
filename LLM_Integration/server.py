from mcp.server.fastmcp import FastMCP
from langchain.vectorstores import FAISS
from langchain.chat_models import init_chat_model
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader, JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain.schema import Document
import os
import json

load_dotenv("../.env")

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm=init_chat_model(model_provider="google_genai",model="gemini-2.0-flash-001",)
embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")

mcp=FastMCP(
    name="RAG_tools",
    host="0.0.0.0",
    port=8000,
)


@mcp.tool()
def get_context_for_llm(query: str) -> list[Document]:
    """
    Function to get context for the LLM based on the query.
    """
    # Load the knowledge base
    loader = JSONLoader(file_path="data/knowledge_base.json", jq_schema='.[]', text_content=False)
    documents = loader.load()
    
    # Create a vector store from the documents
    vectorstore = FAISS.from_documents(documents, embeddings)
    
    # Perform similarity search
    results = vectorstore.similarity_search(query)
    
    # Combine results into a single context string
    context = "\n".join([doc.page_content for doc in results])
    
    return context

@mcp.tool()
def add(a:int , b:int)-> int:
    '''Adds given two numbers'''
    return a+b

@mcp.tool()
def multiply(a:int, b:int)-> int:
    ''' 
    Multiplies given two numbers
    '''
    return a*b

# @mcp.tool()
# def greet_user(msg:str)-> str:
#     '''
#     Greets users
#     '''
#     return f"Hello welcome to Get started with Mcp! "

@mcp.resource("greeting;//{name}")
def get_greeting(name:str)->str:
    '''
    get a personalized greeting
    '''
    return f"Hello {name}"




if __name__=="__main__":
    transport="stdio"
    if(transport=="stdio"):
        print("Starting MCP server on stdio...")
        mcp.run(transport="stdio")
    elif(transport=="sse"):
        print("Starting MCP server on SSE...")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unsupported transport type. Use 'stdio' or 'sse'.{transport}") 

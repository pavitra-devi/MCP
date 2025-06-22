Concepts covered in Modgule 2 : LLM Integration
## creating server with multiple tools:
tools covered in server :
1. get_context_for_llm: This particular tools uses the data from Knowledge base and vector embeddings are created, This tool will fecthses relevant chunks from domain specifc knowledge base
2. add : adds given two integers
3. multiply : multiples given two numbers
4. greet : It's a resource that greets a users

- start the server in stdio or sse transport 

## Creating client and giving access to tools created in server:
helper functions used in client:

1. call_llm : this functions takes given user query and list the available tools from the server, and decides which tool to call based on given user query.
2. convert_to_llm_tool : this helper functions converts server available to tools in model understable tool foormat ( function calling format)
3. run : here server connection and tools iniation takes place.

- note : before running client.py make sure your server is running.
  




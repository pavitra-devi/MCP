## Introduction to MCP :
In this module we will be building our first MCP Server and Client by leveraging simple calculator application.

we will be exploring two types of trransporation mechanisims to establish client and server communication.
Mcp supports the follwing transport mechanisms:

1. Stdio : Standard input and output : This will be used when both client and server in same machine. this is for local development.
2. SSE: Server Sent Events : Through streamable HTTP. This mode of transport can be used when server is in some remote location.

Project setup instructions :
1. set up the virtual environment --> Python -m venv .venv
2. install requirements.txt
3. create server .py with some tools and resources.
4.  start the server by using MCP inspector tool "MCP dev server.py". 
5. create client.py and establish connection between client and server.

### Mcp inspector : 
It 's a great tool for testing our server tools, resources and prompt. It provides user friendly interface to test our server locally. before integrating to client.

# Package managers:
both UV and pip can be used

#commands for using UV:
uv is simple and light weight package manager, comes with many features that eases devlopement work.

- Pip install uv
- uv init project_name : create a project folder with basic files
- uv add mcp[cli]

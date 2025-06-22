# MCP : Model Context protocol
 MCP Has standrdized the way for interaction between LLM and tools . and it is acting as USB-C connector for LLM and tool invocations.

MCP Architecture Overview
The Model Context Protocol follows a client-host-server architecture: This separation of concerns allows for modular, composable systems where each server can focus on a specific domain (like file access, web search, or database operations).

MCP Hosts: Programs like Claude Desktop, IDEs, or your python application that want to access data through MCP
MCP Clients: Protocol clients that maintain 1:1 connections with servers
MCP Servers: Lightweight programs that each expose specific capabilities through the standardized Model Context Protocol (tools, resources, prompts)
Local Data Sources: Your computer’s files, databases, and services that MCP servers can securely access
Remote Services: External systems available over the internet (e.g., through APIs) that MCP servers can connect to
This separation of concerns allows for modular, composable systems where each server can focus on a specific domain (like file access, web search, or database operations).

![image](https://github.com/user-attachments/assets/c53c0ccb-ea2e-4213-a2b9-c66b0f5d93e0)

## Modules:
1. Getting started with MCP : [Calculator server](https://github.com/pavitra-devi/MCP/tree/main/Calculator)
   - In this module we will be creating a Calculator server with basic math operations and client to access the listed tools in server .
2. LLM Integration : [LLM Integration(https://github.com/pavitra-devi/MCP/tree/main/LLM_Integration)
   - In this module we will be diving into integrating our client with gpt model to call specifc tools based on user query. Here LLM autonomusly takes decision which tool to call from the list of available tools from the server.



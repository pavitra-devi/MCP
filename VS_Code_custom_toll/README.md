# Integrating Local MCP servers to github copilot Agent mode

yes, we can integrate our own customly created tools to github copilot Agent mode.
Steps for integration :
1. Go to File --> preferences --> settings --> Search for MCP and enable chat.mcp.discovery.enabled
2. Now create .vscode folder inside root folder of current working directory
3. add mcp.json inside .vscode folder created in earlier step
4. Now link your any custom sever using below shema
 - {
    "inputs": [],
    "servers": {
        "hello-mcp": {
            "command": "d:/mcp/.venv/Scripts/python.exe",
            "args": ["Calculator/server.py"]
        }
    }   

}

Here i have linked server.py from Caluclator module.

5. Now start the server from mcp.json
6. After starting server You can see your custom tool being added to your vs code copilot tool list
   ![image](https://github.com/user-attachments/assets/62dba70c-700c-4965-a8d7-b4c1700707ab)

8. Go to github copilot chat area and Type something related to your tool description.
   - for eg : add 2 +10
     ![image](https://github.com/user-attachments/assets/a848ae57-a1bf-4d9d-a741-7d4ad2d8f521)

9. Now  a pop up will open above the chat area asking permisiion to execute specifc tool from our custom server.
    ![image](https://github.com/user-attachments/assets/6812e115-84e3-453e-afe9-b18833ed528c)
10 . click continue for tool execution





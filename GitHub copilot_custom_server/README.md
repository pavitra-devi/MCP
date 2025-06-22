# Integrating Local MCP servers to github copilot Agent mode

yes, we can integrate our own customly created tools to github copilot Agent mode.
### Steps for integration :
1. Go to File --> preferences --> settings --> Search for MCP and enable chat.mcp.discovery.enabled
2. Now create .vscode folder inside root folder of current working directory
3. add mcp.json inside .vscode folder created in earlier step
4. Now link your any custom sever using below shema
 ![image](https://github.com/user-attachments/assets/5537b094-5ebe-4c39-834c-5b3ecd4fa6d0)


Here i have linked server.py from Caluclator module.

5. Now start the server from mcp.json
6. After starting server You can see your custom tool being added to your vs code copilot tool list
   ![image](https://github.com/user-attachments/assets/62dba70c-700c-4965-a8d7-b4c1700707ab)

8. Go to github copilot chat area and Type something related to your tool description.
   - for eg : add 2 +10

9. Now  a pop up will open above the chat area asking permisiion to execute specifc tool from our custom server.
   ![image](https://github.com/user-attachments/assets/cf741bd0-3a81-493c-bb54-d974d8c33025)

10 . click continue for tool execution





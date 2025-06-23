# MCP
MCP is an open protocol that standardizes how applications provide context to LLMs.

This is a demo project where I have created two MCP model server two test MultiServerMCPClient.
- MCP servers are weather-server.py and mathserver.py
- Client is client.py

# Set up environment
 1] Install Cursor https://www.cursor.com/
  
2] Clone the repo:
   ```bash
   git clone https://github.com/your-org/mcp-demo.git
   cd mcp-demo
   ```

3] For handling virtutal env `uv` has been used.
   ```bash
   uv init
   uv venv
   source .venv/bin/activate
   uv add -r requirements.txt

4] Create a .env file:
   ```bash
   cat .env 
   GROQ_API_KEY = "gsk_xxx"% 
   ```

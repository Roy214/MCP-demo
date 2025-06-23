# MCP
MCP is an open protocol that standardizes how applications provide context to LLMs.

This is a demo project where I have created two MCP model server two test MultiServerMCPClient.
- MCP servers are weather-server.py and mathserver.py
- Client is client.py

# Set up environment
 - Install Cursor
  ~~~
  https://www.cursor.com/
  ~~~
- For handling virtutal env `uv` has been used.
  ~~~
  uv init
  uv venv
  source .venv/bin/activate
  uv add -r requirements.txt
  ~~~


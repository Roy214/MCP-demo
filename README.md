# MCP
MCP is an open protocol that standardizes how applications provide context to LLMs. https://modelcontextprotocol.io/introduction

This is a demo project where I have created two MCP model server two test MultiServerMCPClient.
- MCP servers are weather-server.py and math-server.py
- Client is client.py
- LLM used **qwen-qwq-32b**

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
   ```

4] Create a .env file:
   ```bash
   cat .env 
   GROQ_API_KEY = "gsk_xxx"%
   WEATHER_API_KEY = "9b0af6589b7f4xx"%                                                   
   ```
# Run the code
1] Keep the weather-server.py running 
   ```bash
   python weather-server.py 
   INFO:     Started server process [35777]
   INFO:     Waiting for application startup.
   StreamableHTTP session manager started
   INFO:     Application startup complete.
   ```
2] Run the client.py file
   ```bash
   python client.py 
   Processing request of type ListToolsRequest
   Processing request of type CallToolRequest
   Processing request of type CallToolRequest
   Math response: The result of (5 + 4) - 3 is calculated as follows:

   1. First, perform the addition: 5 + 4 = **9**
   2. Then subtract 3: 9 - 3 = **6**

   Final answer: \boxed{6}
   Weather response: The weather in Bengaluru is **partly cloudy** with a temperature of **22.4°C** and a humidity level of **83%**.
   ```

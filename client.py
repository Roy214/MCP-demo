import argparse

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    DEFAULT_CITY="Bengaluru"
    parser = argparse.ArgumentParser(description="AI weather agent.")
    parser.add_argument("--city", type=str, help="Optional city for request.", default=DEFAULT_CITY)
    args = parser.parse_args()

    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["math-server.py"], ## Ensure correct absolute path
                "transport":"stdio",
            
            },
            "weather": {
                "url": "http://localhost:8000/mcp",  # Ensure server is running here
                "transport": "streamable_http",
            }

        }
    )

    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools=await client.get_tools()
    model=ChatGroq(model="qwen-qwq-32b")
    agent=create_react_agent(
        model,tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (5 + 4) - 3?"}]}
    )

    print("Math response:", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": f"How is the weather like in {args.city}? Please include temperature in Celsius and humidity."}]}
    )
    print("Weather response:", weather_response['messages'][-1].content)

asyncio.run(main())

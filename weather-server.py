from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(city: str) -> str:
    """Get the weather for a given city"""
    return f"The weather in {city} is sunny"

if __name__ == "__main__":
    # The transport is the protocol that the server will use to communicate with the client.
    # In this case, we are using the streamable-http transport, which is the default transport for the MCP server.
    # This means that the server will communicate with the client over the HTTP protocol.
    mcp.run(transport="streamable-http")
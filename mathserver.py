from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def multplication(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    # The transport is the protocol that the server will use to communicate with the client.
    # In this case, we are using the stdio transport, which is the default transport for the MCP server.
    # This means that the server will communicate with the client over the standard input and output streams.   
    mcp.run(transport="stdio")
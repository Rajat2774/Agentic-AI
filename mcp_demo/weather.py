from fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """
    Use this tool whenever the user asks about weather.
    Returns the current weather for the specified location.
    """
    return "it's always raining in California"


if __name__=="__main__":
    mcp.run(transport="streamable-http")
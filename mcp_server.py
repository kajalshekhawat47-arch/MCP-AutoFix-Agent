from mcp.server.fastmcp import FastMCP

print("Starting MCP Server...")

mcp = FastMCP("AutoFixAgent")


@mcp.tool()
def read_logs():
    """
    Read application logs
    """
    try:
        with open("logs/app.log", "r") as file:
            return file.read()

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    print("MCP Server Running...")
    mcp.run()
import os
from semantic_kernel.connectors.mcp import MCPStdioPlugin

async def create_filesystem_plugin():
    target_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "files"))

    plugin = MCPStdioPlugin(
        name="filesystem",
        description="Local Filesystem Plugin",
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            target_folder,
        ],
        load_tools=True,
        load_prompts=False,
        request_timeout=30,
    )

    await plugin.connect()
    return plugin

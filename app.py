import asyncio
import logging
from lights_plugin import LightsPlugin
import os
from dotenv import load_dotenv
load_dotenv()
from semantic_kernel import Kernel
from filesystem_plugin import create_filesystem_plugin
from semantic_kernel.utils.logging import setup_logging
from semantic_kernel.functions import kernel_function
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.functions.kernel_arguments import KernelArguments
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def main():
    kernel = Kernel()

    
    chat_completion = OpenAIChatCompletion(
        ai_model_id="gpt-4.1-nano", 
        api_key=OPENAI_API_KEY
    )

    kernel.add_service(chat_completion)

    
    setup_logging()
    logging.getLogger("kernel").setLevel(logging.DEBUG)

    # Add plugin
    kernel.add_plugin(
        LightsPlugin(),
        plugin_name="Lights",
    )

    filesystem_plugin = await create_filesystem_plugin()
    kernel.add_plugin(filesystem_plugin)

    # Enable planning
    execution_settings = AzureChatPromptExecutionSettings()
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    
    history = ChatHistory()
    history.add_system_message("你可以控制燈光，管理檔案系統，請用繁體中文回答問題。")
   
    userInput = None
    while True:
        userInput = input("User > ")

        # Terminate the loop if the user says "exit"
        if userInput == "exit":
            break

        history.add_user_message(userInput)

        # Get the response from the AI
        result = await chat_completion.get_chat_message_content(
            chat_history=history,
            settings=execution_settings,
            kernel=kernel,
        )

        print("Assistant > " + str(result))

        history.add_message(result)

if __name__ == "__main__":
    asyncio.run(main())
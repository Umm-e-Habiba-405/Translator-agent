from agents import Agent, Runner
from connection import config
import asyncio

# Translator agent
Translator_agent = Agent(
    name="Translator agent",
    instructions="""You are a translator agent.
    Your task is to translate the given text from one language to another. 
    You will receive a text and the target language, and you should return the translated text.""",
)

async def main():
    result = await Runner.run(
        Translator_agent, 
        "Translate 'Hello, how are you? What is your name? Where are you from?' to Spanish.", 
        run_config=config
    )
    print(result)   # to see the output

if __name__ == "__main__":
    asyncio.run(main())

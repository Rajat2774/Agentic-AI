from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

import asyncio
import sys

async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command": sys.executable,
                "args":["math_server.py"],
                "transport":"stdio"
            },
            "weather":{
                "url":"http://localhost:8000/mcp",
                "transport":"streamable-http",
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
  
    model = ChatGroq(model="llama-3.1-8b-instant")

    agent = create_agent(
        model=model,
        tools=tools,
    )

    math_response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What is (3 + 5)"
                }
            ]
        }
    )

    weather_response = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "What is the weather in california. dont use external tools. Use only the get_weather tool "
                    }
                ]
            }
        )

    print(math_response["messages"][-1].content)

    print("    ")
    for msg in weather_response["messages"]:
        print(type(msg), msg)
    

asyncio.run(main())
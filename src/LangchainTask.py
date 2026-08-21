# import api key
import os
from dotenv import load_dotenv

# 1 model defination

from langchain.chat_models import init_chat_model
model = init_chat_model("google_genai:gemini-3.5-flash-lite")

# 2 Tools defination

from langchain_core.tools import tool
import math

@tool
def add(a:float ,b:float) -> float:
    "Add two number . used for an addition operations"
    return a + b

@tool
def multiply(a:float ,b:float) -> float:
    "multiply two number . used for an multiplication operations"
    return a * b

@tool
def divide(a:float ,b:float) -> float:
    "divide two number . used for an division operations"
    return a / b

@tool
def square_root(n:float) -> float:
    "square root of number . used for an calculating square root operations"
    return math.sqrt(n)


tools = [add, multiply,divide,square_root]

# 3 Create an Agent

from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=tools,
)

# 4 run the agent

def run_agent(question: str):
    """Run the agent and print the exceution traces."""
    print(f" User :{question}")
    print("-" * 50 )

    result = agent.invoke({
        "messages": [("user",question)]
    })
    print("Agent :",result["messages"][-1].content)



# Simple : single tool call 
run_agent("What is 42 + 58?")

# Medium : multiplication of tools calls in sequence
run_agent("What is 15 multiplied by 8, then divided by 3")

#Complex: the agent must plan a multi-step approach
run_agent(
    "I have a rectangle with width 12 and height 7."
    "What is its area and what is the square root of the area?"
)

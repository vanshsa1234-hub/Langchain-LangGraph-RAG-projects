from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool

model=ChatGroq(model="openai/gpt-oss-120b")
search=GoogleSerperAPIWrapper()

@tool
def google_search(query: str) -> str:
    """Search Google for current and up-to-date information."""
    return search.run(query)

agent=create_agent(
    model=model,
    tools=[google_search],
    system_prompt="You are a agent and can search for any question on google "
)

while True:
    query=input("User: ")
    if query.lower()=="quit":
        print("Good Bye")
        break

    response=agent.invoke({"messages":[{"role":"user", "content":query}]})
    print("AI: ",response["messages"][-1].content)
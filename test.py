from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
llm=ChatGroq(model="openai/gpt-oss-120b")


while True:
    query=input("user:")

    if query.lower() in {"exit","bye","quit"}:
        break
    res=llm.invoke(query)
    print("ai: ",res.content)
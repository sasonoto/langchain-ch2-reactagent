from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch


# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-ch2-reactagent!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer in chicago")})
    print(result)


if __name__ == "__main__":
    main()


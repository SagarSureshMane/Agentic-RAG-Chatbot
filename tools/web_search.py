from langchain_core.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

@tool
def web_search(query: str) -> str:
    """
    Search the internet for current information.
    Use for latest news, recent events, and web-based facts.
    """

    try:
        response = client.search(
            query=query,
            max_results=5
        )

        output = []

        for result in response["results"]:
            output.append(
                f"Title: {result['title']}\n"
                f"Content: {result['content']}\n"
                f"URL: {result['url']}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Web Search Error: {str(e)}"
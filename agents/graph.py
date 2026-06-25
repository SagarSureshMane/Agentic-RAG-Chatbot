from dotenv import load_dotenv



from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

# Tools
from tools.calculator import calculator
from tools.web_search import web_search
from tools.wikipedia_tool import wikipedia_search
from tools.rag_tool import rag_search
from tools.sql_tool import sql_query
from tools.email_tool import send_email
from tools.pdf_tool import read_pdf
from tools.excel_tool import analyze_excel

load_dotenv()
def build_agent():
 llm = ChatOpenAI( 
    model="gpt-4o-mini",
    temperature=0)

 tools = [
     calculator,
     web_search,
     wikipedia_search,
     rag_search,
     sql_query,
     send_email,
     read_pdf,
     analyze_excel


     
    ]
 agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt="""
    You are an Agentic RAG Assistant.

    If the user asks about:
    - uploaded documents
    - PDFs
    - document summaries
    - file contents

    ALWAYS use the rag_search tool first.

    Do not ask the user to upload a file if one may already exist in the knowledge base.
    """
 )
 
 return agent
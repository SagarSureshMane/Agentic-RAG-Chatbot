from langchain_core.tools import tool
from rag.retriever import get_retriever

@tool
def rag_search(query: str) -> str:
    """
    Search uploaded documents.

    Use this tool whenever:
    - user asks about uploaded PDF
    - user asks about uploaded document
    - user asks to summarize document
    - user asks questions from uploaded files
    """
    print("RAG TOOL CALLED:", query)
    retriever = get_retriever()

    docs = retriever.invoke(query)

    if not docs:
        return "No relevant documents found."

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )

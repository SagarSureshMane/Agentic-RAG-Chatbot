from langchain_core.tools import tool
from pypdf import PdfReader

@tool
def read_pdf(path: str) ->str:
    """
    Read PDF content
    """
    try:
        reader = PdfReader(path)
        text = " "
        for page in reader.pages:
            text+= page.extract_text()
        return text[:10000]
    
    except Exception as e:
        return str(e)
    

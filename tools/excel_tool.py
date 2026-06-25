from langchain_core.tools import tool
import pandas as pd

@tool
def analyze_excel(path:str)-> str:
    """
    Analyze Excel tool
    """
    try:
        df = pd.read_excel(path)
        return f"""
 columns:
 {df.columns.tolist()}

 Rows:
 {len(df)}

 Summary:
 {df.describe(include='all').to_string()}
"""
    except Exception as e:
        return str(e)
    

from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    Example: 10+20*5
    """
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

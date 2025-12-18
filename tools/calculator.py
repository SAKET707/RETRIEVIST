import math
from langchain_core.tools import tool


@tool
def calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression and return the result.

    Supports basic arithmetic and math functions such as:
    +, -, *, /, **, sqrt, sin, cos, log, etc.
    """
    allowed_names = {
        k: v for k, v in math.__dict__.items() if not k.startswith("__")
    }

    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"

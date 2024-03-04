import ast
from langchain.tools import tool


@tool
def do_sum(values_str: str) -> int | float:
    """calculate the sums of a list of numbers, valid input likes : '[1,2,3,4]' """
    values : list = ast.literal_eval(values_str)
    return sum(values)

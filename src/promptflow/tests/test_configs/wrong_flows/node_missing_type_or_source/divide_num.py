from promptflow.core import tool


@tool
def divide_num(num: int) -> int:
    return (int)(num / 2)

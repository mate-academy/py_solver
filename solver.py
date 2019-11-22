"""solve module"""


def solve(expr: str) -> int:
    """solve_"""
    operations = ["+", "-", "*", "/"]
    for i in expr:
        if not i.isdigit() and i not in operations:
            raise ValueError
    return eval(expr)

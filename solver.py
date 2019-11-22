"""
solve math expression evaluation
"""


def precedence(operation: str) -> int:
    """
    Return precedence of math operation.
    :param operation: str
    :return: int
    """
    if operation in ('+', '-'):
        return 1
    if operation in ('*', '/'):
        return 2
    return 0


def apply_math_operation(frst_num: float, sec_num: float, operation: str) -> float:
    """
    Calculate the value between two numbers.
    :param frst_num: float
    :param sec_num: float
    :param operation: str
    :return: float
    """
    if operation == '+':
        return frst_num + sec_num
    if operation == '-':
        return frst_num - sec_num
    if operation == '*':
        return frst_num * sec_num
    if operation == '/':
        return frst_num // sec_num


def solve(math_expr: str) -> int:
    """
    Evaluate arithmetic expressions in a string representation.
    An expression can include integers and operators +, -, *, /.
    :param math_expr: str
    :return: int
    """
    i = 0
    ops_stack = []
    values_stack = []

    while i < len(math_expr):
        if math_expr[i].isdigit():
            values_stack.append(math_expr[i])
        else:
            while len(ops_stack) != 0 and precedence(ops_stack[-1]) >= precedence(math_expr[i]):
                frst_num = values_stack.pop()
                sec_num = values_stack.pop()
                operation = ops_stack.pop()
                result = apply_math_operation(int(sec_num), int(frst_num), operation)
                values_stack.append(result)

            ops_stack.append(math_expr[i])
        i += 1

    while len(ops_stack) != 0:
        frst_num = values_stack.pop()
        sec_num = values_stack.pop()
        operation = ops_stack.pop()
        result = apply_math_operation(int(sec_num), int(frst_num), operation)
        values_stack.append(result)

    return int(values_stack[-1])

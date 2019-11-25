"""
docstring
"""

OPERATORS = {'+', '-', '*', '/'}
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}


def solve(expr: str) -> int:
    """

    :param expr:
    :return:
    """
    return eval_postfix(to_postfix(expr))


def to_postfix(expr):
    """

    :param expr:
    :return:
    """
    stack = []
    res = ''
    for char in expr:
        if char not in OPERATORS:
            res += char
        else:
            while stack and PRIORITY[char] <= PRIORITY[stack[-1]]:
                res += stack.pop()
            stack.append(char)
    while stack:
        res += stack.pop()
    return res


def eval_postfix(expr):
    """

    :param expr:
    :return:
    """
    stack = []
    for char in expr:
        if char not in OPERATORS:
            stack.append(int(char))
        else:
            b_ch = stack.pop()
            a_ch = stack.pop()
            c_ch = {'+': a_ch+b_ch, '-': a_ch-b_ch, '*': a_ch*b_ch, '/': a_ch/b_ch}[char]
            stack.append(c_ch)
    return int(stack[-1])

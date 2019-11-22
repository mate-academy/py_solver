"""solver module"""

def solve(expr):
    """
    Returns calculated numerical value
    of a given expression
    """
    lis_expr = []

    for char in expr:
        try:
            lis_expr.append(int(char))
        except ValueError:
            lis_expr.append(char)

    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b}

    for oper in '*/+-':
        while oper in lis_expr:
            idx = lis_expr.index(oper)
            res = operators[oper](lis_expr[idx - 1], lis_expr[idx + 1])
            lis_expr[idx - 1:idx + 2] = [res]

    return lis_expr[0]

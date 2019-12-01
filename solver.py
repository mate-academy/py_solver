""" similar arithmetic operation"""


def solve(str_expr: str) -> int:
    """ return result"""
    operation = []
    number = []
    for i in str_expr:
        if i.isdigit():
            number.append(int(i))
        else:
            operation.append(i)

    while operation:
        for i in operation:
            if i == "*":
                number.insert(operation.index(i),
                              number.pop(operation.index(i) + 1) * number.pop(operation.index(i)))
                operation.pop(operation.index(i))
        for i in operation:
            if i == "/":
                number.insert(operation.index(i),
                              int(1/number.pop(operation.index(i)+1)
                                  * number.pop(operation.index(i))))
                operation.pop(operation.index(i))
        for i in operation:
            if i == "+":
                number.insert(operation.index(i),
                              number.pop(operation.index(i) + 1) + number.pop(operation.index(i)))
                operation.pop(operation.index(i))
        for i in operation:
            if i == "-":
                number.insert(operation.index(i),
                              - number.pop(operation.index(i) + 1) + number.pop(operation.index(i)))
                operation.pop(operation.index(i))

    return number[0]

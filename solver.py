"""
Arithmetic expressions in a string representation
"""

def solve(expr: str) -> int:
    """ arithmetic expressions """
    lst = list(expr)

    while '*' in lst:
        lst, indx, num1, num2 = find_numbs(lst, '*')
        lst[indx-1] = str(int(num1) * int(num2))

    while '/' in lst:
        lst, indx, num1, num2 = find_numbs(lst, '/')
        lst[indx-1] = str(int(int(num1) / int(num2)))

    while '+' in lst:
        lst, indx, num1, num2 = find_numbs(lst, '+')
        lst[indx-1] = str(int(num1) + int(num2))

    while '-' in lst:
        lst, indx, num1, num2 = find_numbs(lst, '-')
        lst[indx-1] = str(int(num1) - int(num2))

    return int(''.join(lst))


def find_numbs(lst, sign):
    """ Find numbers """
    indx = lst.index(sign)
    num1, num2 = lst.pop(indx - 1), lst.pop(indx)
    return lst, indx, num1, num2

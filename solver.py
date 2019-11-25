"""The function to evaluate arithmetic expressions in a string
representation.
"""


def solve(expr: str) -> int:
    """General function"""
    expr_list = list(expr)

    for i in expr:
        if i == '*':
            expr_list = multiplying(expr_list)
        elif i == '/':
            expr_list = division(expr_list)

    for i in expr:
        if i == '+':
            expr_list = addition(expr_list)
        if i == '-':
            expr_list = subtraction(expr_list)

    return int(expr_list[0])


def multiplying(arr):
    """Helper for multiplying"""
    sing_index = arr.index('*')
    multipl_product = int(arr[sing_index-1]) \
                      * int(arr[sing_index+1])
    arr.remove('*')
    arr.insert(sing_index, multipl_product)
    arr.pop(sing_index + 1)
    arr.pop(sing_index - 1)
    return arr


def division(arr):
    """Helper for division"""
    sing_index = arr.index('/')
    divis_product = int(arr[sing_index - 1]) \
                    / int(arr[sing_index + 1])
    arr.remove('/')
    arr.insert(sing_index, divis_product)
    arr.pop(sing_index + 1)
    arr.pop(sing_index - 1)
    return arr


def subtraction(arr):
    """Helper for subtraction"""
    sing_index = arr.index('-')
    substr_product = int(arr[sing_index - 1]) \
                    - int(arr[sing_index + 1])
    arr.remove('-')
    arr.insert(sing_index, substr_product)
    arr.pop(sing_index + 1)
    arr.pop(sing_index - 1)
    return arr


def addition(arr):
    """Helper for addition"""
    sing_index = arr.index('+')
    add_product = int(arr[sing_index - 1]) \
                     + int(arr[sing_index + 1])
    arr.remove('+')
    arr.insert(sing_index, add_product)
    arr.pop(sing_index + 1)
    arr.pop(sing_index - 1)
    return arr

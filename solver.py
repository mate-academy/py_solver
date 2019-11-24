"""docstring"""


class Stack:
    """stack"""
    def __init__(self):
        self.items = []

    def push(self, item):
        """push"""
        self.items.append(item)

    def pop(self):
        """pop"""
        return self.items.pop()


def solve(expr):
    """solver"""
    char_list = []
    for char in expr:
        if char.isdigit():
            char_list.append(int(char))
        else:
            char_list.append(char)

    stack = Stack()
    i = 0
    while i < len(char_list):
        if char_list[i] == "*":
            prod = stack.pop() * char_list[i+1]
            stack.push(prod)
            i += 2
        elif char_list[i] == "/":
            div = stack.pop() / char_list[i + 1]
            stack.push(div)
            i += 2
        else:
            stack.push(char_list[i])
            i += 1

    char_list = stack.items.copy()
    stack.items = []
    j = 0
    while j < len(char_list):
        if char_list[j] == "+":
            prod = stack.pop() + char_list[j + 1]
            stack.push(prod)
            j += 1
        elif char_list[j] == "-":
            div = stack.pop() - char_list[j + 1]
            stack.push(div)
            j += 1
        else:
            stack.push(char_list[j])
        j += 1

    return stack.pop()

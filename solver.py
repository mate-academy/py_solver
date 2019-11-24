class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def solve(expr: str) -> int:
    char_list = [char for char in expr]
    print(char_list)

    stack = Stack()
    i = 0
    while i < len(char_list):
        if char_list[i] == "*":
            prod = stack.pop() * int(char_list[i+1])
            stack.push(prod)
            i += 2
        elif char_list[i] == "/":
            div = stack.pop() / int(char_list[i + 1])
            stack.push(int(div))
            i += 2
        else:
            if char_list[i].isdigit():
                stack.push(int(char_list[i]))
                i += 1
            else:
                stack.push(char_list[i])
                i +=1
    char_list = stack.items.copy()
    print(char_list)
    stack.items = []
    i = 0
    while i < len(char_list):
        if char_list[i] == "+":
            print("+")
            prod = stack.pop() + char_list[i + 1]
            stack.push(prod)
            i += 1
        elif char_list[i] == "-":
            print("-")
            div = stack.pop() - char_list[i + 1]
            stack.push(div)
            i += 1
        else:
            print("els")
            stack.push(char_list[i])
        i += 1
    return(stack.items)


print(solve("2+2"))


"""module docstring"""

def final_count(array):
    """when the array elements are multiplied and/or divided
    adding up and subtraction is executed"""
    lump_sum = 0
    for seq, _value in enumerate(array):
        if array[seq] == "+":
            lump_sum += int(array[seq + 1])
            seq += 1
        elif array[seq] == "-":
            lump_sum -= int(array[seq + 1])
            seq += 1
        seq += 1
    return lump_sum


def solve(expression):
    """main function: string expression is first analysed for multiplication
    and/or subtraction and subsequently - for adding up and subtraction"""
    integers = []
    integers_count = -1
    number = 0
    while number < len(expression):
        integers.append(expression[number])
        integers_count += 1
        if expression[number] == "*":
            integers[(integers_count - 1):(integers_count + 1)] = \
                [int(integers[integers_count - 1]) * int(expression[number+1])]
            integers_count -= 1
            number += 1
        if expression[number] == "/":
            integers[(integers_count - 1):(integers_count + 1)] = \
                [int(integers[integers_count - 1]) / int(expression[number + 1])]
            integers_count -= 1
            number += 1
        number += 1

    result = int(integers[0]) + final_count(integers)

    return result

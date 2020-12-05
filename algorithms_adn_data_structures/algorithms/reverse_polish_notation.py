import operator

from data_structures.my_stack import StackList
from algorithms.braces_sequences import is_braces_sequence_correct


def converter_to_rpn_format(expression: str) -> list:
    result_array = []
    if not is_braces_sequence_correct(expression):
        return result_array

    op_stack = StackList()  # operational stack
    numbers = [str(x) for x in range(10)]
    p1_operations = "*/"  # priority 1 operations
    p2_operations = "+-"  # priority 1 operations
    braces = ["(", ")"]
    operations = p1_operations + p2_operations
    flag_for_pass = 0  # this flag used for adding numbers to result array
    for index, i in enumerate(expression):
        if flag_for_pass:
            flag_for_pass -= 1
            continue

        if i in braces:
            if i == braces[0]:
                op_stack.push(i)
            else:
                for _ in range(op_stack.get_size()):
                    if op_stack.top() != braces[0]:
                        result_array.append(op_stack.pop())
                    else:
                        op_stack.pop()
                        break
                continue

        elif i in operations:
            if op_stack.is_empty() or (
                    op_stack.top() in p2_operations
                    and i in p1_operations
            ) or (op_stack.top() in braces[0]):
                op_stack.push(i)
            else:
                result_array.append(op_stack.pop())
                op_stack.push(i)

        elif i in numbers:
            result_number = expression[index]
            for k in range(1, len(expression) - index + 1):
                try:
                    if expression[index + k] in numbers:
                        result_number += expression[index + k]
                    else:
                        result_array.append(int(result_number))
                        flag_for_pass = len(result_number) - 1
                        break
                except IndexError:
                    result_array.append(int(result_number))
                    flag_for_pass = len(result_number) - 1
                    break

    for _ in range(op_stack.get_size()):
        result_array.append(op_stack.pop())

    return result_array


def rpn_algorithm(array: str):
    """
    https://habr.com/ru/post/282379/
    :param array: array of polish something strange
    :return: result of expression
    """
    rpn_array = converter_to_rpn_format(array)
    stack = StackList()
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,  # use operator.div for Python 2
    }
    for i in rpn_array:
        if isinstance(i, int):
            stack.push(i)
        else:
            y = stack.pop()
            x = stack.pop()
            stack.push(ops[i](x, y))

    return stack.pop()


if __name__ == "__main__":
    exp = "2+7*5"
    exp_2 = "(2+7)*5"
    exp_3 = "(6+10-4)/(1+1*2)+1"
    result = rpn_algorithm(exp)
    assert result == 37
    result = rpn_algorithm(exp_2)
    assert result == 45
    result = rpn_algorithm(exp_3)
    assert result == 5

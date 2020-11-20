from algorithms.my_stack import MyStack


def rpn_algorithm(array: list):
    """
    https://habr.com/ru/post/282379/
    :param array: array of polish something strange
    :return: result of expression
    """
    stack = MyStack()
    for i in array:
        if isinstance(i, int):
            stack.push(i)
        else:
            y = stack.pop()
            x = stack.pop()
            stack.push(eval(str(x) + i + str(y)))

    return stack.pop()


if __name__ == "__main__":
    # 2 + 7 * 5
    exp = [2, 7, 5, "*", "+"]
    # (2 + 7) * 5
    exp_2 = [2, 7, "+", 5, "*"]
    # (6 + 10 - 4) / (1 + 1 * 2) + 1
    exp_3 = [6, 10, "+", 4, "-", 1, 1, 2, "*", "+", "/", 1, "+"]
    result = rpn_algorithm(exp)
    assert result == 37
    result = rpn_algorithm(exp_2)
    assert result == 45
    result = rpn_algorithm(exp_3)
    assert result == 5

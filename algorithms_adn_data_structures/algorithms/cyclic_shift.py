def cyclic_shift_left(a_list: list) -> None:
    """
    Function for cyclic shift process to left
    :param a_list: list
    :return: None
    """
    tmp = a_list[0]
    for i in range(len(a_list) - 1):
        a_list[i] = a_list[i + 1]
    a_list[len(a_list) - 1] = tmp


def cyclic_shift_right(a_list: list) -> None:
    """
    Function for cyclic shift process to right
    :param a_list: list
    :return: None
    """
    tmp = a_list[len(a_list) - 1]
    for i in range(len(a_list) - 2, -1, -1):
        a_list[i + 1] = a_list[i]
    a_list[0] = tmp


if __name__ == '__main__':
    test_array = [1, 2, 3, 4, 5, 6, 7]
    cyclic_shift_left(test_array)
    assert test_array == [2, 3, 4, 5, 6, 7, 1]
    cyclic_shift_right(test_array)
    assert test_array == [1, 2, 3, 4, 5, 6, 7]

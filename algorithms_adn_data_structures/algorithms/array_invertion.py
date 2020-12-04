def invert_array(a_list: list) -> None:
    """
    Function for array invert
    :param a_list: Array to invert
    :return: None
    """
    n = len(a_list)
    for i in range(n//2):
        a_list[i], a_list[n - 1 - i] = a_list[n - 1 - i], a_list[i]


if __name__ == '__main__':
    test_array_1 = [-11, -22, -33, -44, -55, -66, -77]
    test_array_2 = [1, 2, 3, 4, 5, 6, 7]
    test_array_3 = [0, 2, 5, 65, 78, 4, 2, 47]
    arrays = [test_array_1, test_array_2, test_array_3]
    for i in arrays:
        invert_array(i)
        print(i)

    assert test_array_1 == [-77, -66, -55, -44, -33, -22, -11]
    assert test_array_2 == [7, 6, 5, 4, 3, 2, 1]
    assert test_array_3 == [47, 2, 4, 78, 65, 5, 2, 0]

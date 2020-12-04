# ------- bound help in case when we have repeated numbers in array -------
def left_bound(a_list: list, key: int):
    left = -1
    right = len(a_list)
    while right - left > 1:
        mid = (left + right) // 2
        if a_list[mid] < key:
            left = mid
        else:
            right = mid

    return left


def right_bound(a_list: list, key: int):
    left = -1
    right = len(a_list)
    while right - left > 1:
        mid = (left + right) // 2
        if a_list[mid] <= key:
            left = mid
        else:
            right = mid

    return right


def find_numbers(a_list: list, key: int):
    lb = left_bound(a_list, key)
    rb = right_bound(a_list, key)

    return a_list[lb + 1:rb]


# ------- This one will help find any of searching elements -------
def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)


if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 7, 8, 9, 9]
    result = find_numbers(test_array, 7)
    assert result == [7, 7, 7, 7]
    print(result)
    index = binary_search_recursive(test_array, 7, 0, 14)
    print(index)

# This sorting algorithms have O(N**2) complexity
def insertion_sort(a_list: list) -> None:
    """
    Sorting by insertion
    :param a_list: list
    :return: None
    """
    N = len(a_list)
    for n in range(1, N):
        i = n
        while i > 0 and a_list[i - 1] > a_list[i]:
            a_list[i], a_list[i - 1] = a_list[i - 1], a_list[i]
            i -= 1


def choice_sort(a_list: list) -> None:
    """
    Sorting by choice method
    :param a_list: list
    :return: None
    """
    N = len(a_list)
    for pos in range(0, N-1):
        for i in range(pos+1, N):
            if a_list[i] < a_list[pos]:
                a_list[i], a_list[pos] = a_list[pos], a_list[i]


def bubble_sort(a_list: list) -> None:
    """
    Sorting by bubble method
    :param a_list: list
    :return: None
    """
    N = len(a_list)
    for bypass in range(1, N):
        for i in range(0, N-bypass):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]

    # another implementation
    # swapped = True
    # while swapped:
    #     swapped = False
    #     for i in range(len(a_list) - 1):
    #         if a_list[i] > a_list[i + 1]:
    #             a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
    #             swapped = True


# O(N)
def count_sort(a_list: list) -> None:
    frequency_list_len = max(a_list) + 1
    frequency_list = [0] * frequency_list_len
    for i in a_list:
        frequency_list[i] += 1

    i = 0
    for k in range(frequency_list_len):
        for m in range(frequency_list[k]):
            a_list[i] = k
            i += 1

# O(n log n)
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


def test_list_generator() -> tuple:
    test_list = list(range(10, 21)) + list(range(10))
    sorted_list = list(range(21))

    return test_list, sorted_list


def test_sort_algorithm(sort_algorithm):
    test_list, sorted_list = test_list_generator()
    sort_algorithm(test_list)
    assert test_list == sorted_list


def test_count_quick_sort_algorithm(sort_algorithm):
    # test_list, sorted_list = test_list_generator()
    # sort_algorithm(test_list)
    # assert test_list == sorted_list
    test_list = [7, 6, 3, 3, 3, 5, 5, 7, 8, 21, 13, 14, 13]
    sorted_list = [3, 3, 3, 5, 5, 6, 7, 7, 8, 13, 13, 14, 21]
    sort_algorithm(test_list)
    assert test_list == sorted_list


if __name__ == "__main__":
    test_sort_algorithm(insertion_sort)
    test_sort_algorithm(choice_sort)
    test_sort_algorithm(bubble_sort)
    test_count_quick_sort_algorithm(count_sort)
    test_count_quick_sort_algorithm(quick_sort)

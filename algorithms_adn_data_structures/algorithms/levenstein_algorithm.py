def levenshtein_distance(a: str, b: str) -> int:
    """
    O(M * N)
    Search of distance between two words:
    the minimum number of single-character edits
    (insertions, deletions or substitutions)
    required to change one word into the other
    https://www.youtube.com/watch?v=We3YDTzNXEk - video explanation

    :param a: string
    :param b: string
    :return: length of minimal distance (int)
    """
    result_array = [
        [i + j if i * j == 0 else 0 for j in range(len(b) + 1)]
        for i in range(len(a) + 1)
    ]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                result_array[i][j] = result_array[i - 1][j - 1]
            else:
                result_array[i][j] = 1 + min(
                    result_array[i - 1][j],
                    result_array[i][j - 1],
                    result_array[i - 1][j - 1]
                )

    return result_array[len(a)][len(b)]


if __name__ == "__main__":
    test_string_1 = "BIG"
    test_string_2 = "AMBIGUOUS"
    result = levenshtein_distance(test_string_1, test_string_2)
    print(result)

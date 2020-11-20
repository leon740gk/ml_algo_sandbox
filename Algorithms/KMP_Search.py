def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1
    lps[0] = 0
    while i < m:
        if pattern[i] == pattern[length]:
            lps[i] = length + 1
            length += 1
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def kmp_search(pattern: str, search_string: str):
    """
    Knuth-Morris-Pratt algorithm | String Matching Algorithm | Substring Search
    https://www.youtube.com/watch?v=4jY57Ehc14Y - video explanation

    :param pattern: substring for matching in string
    :param search_string: string for perform search
    :return: indexes of substring occurrences (print in this case)
    """
    n = len(search_string)
    m = len(pattern)

    lps = [0] * m  # longest prefix suffix array for pattern
    compute_lps_array(pattern, m, lps)
    i = j = 0  # pointer for pattern and search_string
    while i < n - m + 1:
        if search_string[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == m:
            print(f"substring found at index {i - j}")
            j = lps[j - 1]


if __name__ == "__main__":
    string_for_search = "THIS TEXT IS JUST TEXT FOR TEST IN TEXT SEARCH"
    substring = "TEXT"
    kmp_search(substring, string_for_search)

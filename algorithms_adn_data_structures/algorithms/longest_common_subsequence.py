from time import time


def lcs(x, y, m, n):
    """largest common subsequence"""
    if m == 0 or n == 0:
        return 0
    elif x[m - 1] == y[n - 1]:
        return 1 + lcs(x, y, m - 1, n - 1)
    else:
        return max(lcs(x, y, m, n - 1), lcs(x, y, m - 1, n))


def lcs_2(x, y):
    """largest common subsequence"""

    # find the length of the strings
    m = len(x)
    n = len(y)

    # declaring the array for storing the dp values
    result_array = [[0] * (n + 1) for _ in range(m + 1)]

    """Following steps build result_array[m + 1][n + 1] in bottom up fashion 
    Note: result_array[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                result_array[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                result_array[i][j] = result_array[i - 1][j - 1] + 1
            else:
                result_array[i][j] = max(result_array[i - 1][j], result_array[i][j - 1])

                # result_array[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return result_array[m][n]


if __name__ == "__main__":
    X = "AGGTABFGFDS"
    Y = "GXTXAYBDFFHD"
    start_lcs = time()
    print("Length of LCS is ", lcs(X, Y, len(X), len(Y)))
    finish_lcs = time()
    elapsed_time = finish_lcs - start_lcs
    print(f"lcs took: {elapsed_time} time")

    start_lcs = time()
    print("Length of LCS is ", lcs_2(X, Y))
    finish_lcs = time()
    elapsed_time = finish_lcs - start_lcs
    print(f"lcs_2 took: {elapsed_time} time")

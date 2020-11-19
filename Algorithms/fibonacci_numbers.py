def fib_1(n: int) -> int:
    if n <= 1:
        return n
    return fib_1(n - 1) + fib_1(n - 2)


def fib_2(n: int) -> int:
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


if __name__ == "__main__":
    result = fib_1(7)
    assert result == 13
    result = fib_2(7)
    assert result == 13

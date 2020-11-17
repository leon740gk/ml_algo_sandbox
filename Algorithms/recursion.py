# import graphics as gr
#
#
# window = gr.GraphWin("Recursion", 740, 740)
#
#
# def fractal_rectangle(
#         A: tuple,
#         B: tuple,
#         C: tuple,
#         D: tuple,
#         depth=10,
#         alpha=0.1
# ) -> None:
#
#     if depth < 1:
#         return
#     for M, N in (A, B), (B, C), (C, D), (D, A):
#         gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
#     A1 = (
#         A[0] * (1 - alpha) + B[0] * alpha,
#         A[1] * (1 - alpha) + B[1] * alpha
#     )
#     B1 = (
#         B[0] * (1 - alpha) + C[0] * alpha,
#         B[1] * (1 - alpha) + C[1] * alpha
#     )
#     C1 = (
#         C[0] * (1 - alpha) + D[0] * alpha,
#         C[1] * (1 - alpha) + D[1] * alpha
#     )
#     D1 = (
#         D[0] * (1 - alpha) + A[0] * alpha,
#         D[1] * (1 - alpha) + A[1] * alpha
#     )
#
#     fractal_rectangle(A1, B1, C1, D1, depth=depth - 1)


def factorial(n: int) -> int:
    """
    n! = (n -1)! * n
    """
    assert n >= 0, "Only positive integers!"
    if n == 0:
        return 1
    return factorial(n - 1) * n


def gcd(a: int, b: int) -> int:
    """
    Euclidean algorithm
    """
    return a if b == 0 else gcd(b, a % b)


def quick_pow(a: float, n: int):
    if n == 0:
        return 1
    if n % 2 == 1:
        return quick_pow(a, n - 1) * a
    else:
        return quick_pow(a ** 2, n // 2)


def generate_rotations(n: int, m: int, prefix=None):
    """
    Generator of rotations
    :param n: Notation
    :param m: Amount of numbers
    """
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for i in range(n):
        prefix.append(i)
        generate_rotations(n, m - 1, prefix)
        prefix.pop()


def generate_permutations(n: int, m: int=-1, prefix=None):
    """
    :param n: amount of numbers
    :param m: amount of permutations
    """
    m = n if m == -1 else m
    prefix = prefix or []
    if m == 0:
        print(*prefix)
        return
    for number in range(1, n + 1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()


if __name__ == '__main__':
    # A = (100, 100)
    # B = (500, 100)
    # C = (500, 500)
    # D = (100, 500)
    # fractal_rectangle(A, B, C, D, 47)
    # n = 13
    # result = factorial(n)
    # print(f"factorial n = {result}")
    # a = 44
    # b = 24
    # result = gcd(a, b)
    # print(f"gcd for {a} and {b} = {result}")
    # num = 7.4
    # power = 13
    # result = quick_pow(num, power)
    # print(f"{num} in pow {power} = {result}")
    # generate_rotations(2, 3)
    generate_permutations(3)

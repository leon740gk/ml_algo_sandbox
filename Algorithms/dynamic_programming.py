"""
Task: grasshopper can leap from point A to point B in 3 different ways:
1. +1 leap
2. +2 leaps
3. +3 leaps
0__~%o>__2__3__4__5__6__7____N
Also we have an array (of boolean values) of not allowed point tp leap
e.g. [0, 1, 1, 1, 1, 0, 0, 0]
0__~%o>__(2)allowed__(3)allowed__(4)allowed__
(5)not_allowed__(6)not_allowed__(7)not_allowed____N

Task is to count all different trajectories for reaching N point by grasshopper
"""
def count_trajectories(n: int, allowed: list) -> int:
    T = [0, 1, allowed[2]] + [0] * (n - 2)
    for i in range(3, n):
        if allowed[i]:
            T[i] = T[i - 1] + T[i - 2] + T[i - 3]

    return max(T)


"""
Task: grasshopper can leap from point A to point B in 2 different ways:
1. +1 leap
2. +2 leaps
0__~%o>__2__3__4__5__6__7____N
Also we have an array of prices for visiting every slot in a path

Task is to count minimal cost of designation to point N
"""
def min_cost_count(n: int, price: list):
    min_cost_array = [
        float("-inf"),
        price[1],
        price[1] + price[2]
    ] + [0] * (n - 2)
    for i in range(3, n + 1):
        min_cost_array[i] = price[i] + min(
            min_cost_array[i - 1],
            min_cost_array[i - 2]
        )

    return min_cost_array[n]


if __name__ == "__main__":
    allowed = [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    result = count_trajectories(n=7, allowed=allowed)
    assert result == 5
    print(result)
    price = [0, 4, 6, 7, 10, 13, 14, 21, 47]
    result = min_cost_count(n=7, price=price)
    assert result == 45
    print(result)

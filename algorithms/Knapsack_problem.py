# https://www.youtube.com/watch?v=cJ21moQpofY - video explanation

# A naive recursive implementation of 0-1 Knapsack Problem

# Returns the maximum value that can be put in a knapsack of
# capacity W
def knapsack_recur(w, wt, val, n):
    # Base Case
    if n == 0 or w == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if wt[n - 1] > w:
        return knapsack_recur(w, wt, val, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n - 1] + knapsack_recur(w - wt[n - 1], wt, val, n - 1),
            knapsack_recur(w, wt, val, n - 1)
        )


# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W
def knapsack(w, wt, val, n):
    k = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(w + 1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif wt[i - 1] <= w:
                k[i][w] = max(
                    val[i - 1] + k[i - 1][w - wt[i - 1]],
                    k[i - 1][w]
                )
            else:
                k[i][w] = k[i - 1][w]

    return k[n][w]


if __name__ == "__main__":
    values_of_items = [60, 100, 120]
    weight_of_items = [10, 20, 30]
    knapsack_capacity = 50
    n_items = len(values_of_items)
    print(
        knapsack(knapsack_capacity, weight_of_items, values_of_items, n_items)
    )

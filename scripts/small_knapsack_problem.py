# Challenge #20 - Intermediate
# Small Knapsack Problem (Dynamic Programming)
# Objective: Practice optimization, nested loops, and table-based dynamic programming

"""
Solve a small version of the 0/1 Knapsack problem using Dynamic Programming.

Given a limited capacity and a few items (each with weight and value),
find the maximum total value that can be carried without exceeding the capacity.
Helps build intuition for optimization and table-based algorithms.
"""

def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Return the maximum value achievable within the given capacity.
    Uses a bottom-up Dynamic Programming approach.
    """
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build DP table row by row
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight fits in the current capacity
            if weights[i - 1] <= w:
                # Decide to take or skip the item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],  # take it
                    dp[i - 1][w]                                   # skip it
                )
            else:
                dp[i][w] = dp[i - 1][w]  # can't take this item

    return dp[n][capacity]


# Example test
weights = [2, 3, 4, 5]
values = [10, 20, 30, 40]
capacity = 5

max_value = knapsack(weights, values, capacity)
print(f"Maximum value for capacity {capacity}: {max_value}")

# Challenge #68 - Intermediate
# Unique Paths in a Grid
# Objective: Count unique paths using Dynamic Programming.

"""
Count the number of unique paths in an m x n grid.
Movement is restricted to right and down only.
Demonstrates dynamic programming and state transition logic.
"""

def unique_paths(m: int, n: int) -> int:
    """Return number of unique paths from top-left to bottom-right."""
    dp = [[0] * n for _ in range(m)]   # create DP table

    # first row: only one way (move right)
    for j in range(n):
        dp[0][j] = 1

    # first column: only one way (move down)
    for i in range(m):
        dp[i][0] = 1

    # fill the rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # from top + left

    return dp[m - 1][n - 1]   # bottom-right corner


if __name__ == "__main__":
    rows = int(input("Enter number of rows (m): ").strip())
    cols = int(input("Enter number of columns (n): ").strip())

    result = unique_paths(rows, cols)
    print(f"Unique paths in a {rows}x{cols} grid: {result}")

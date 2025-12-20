# Challenge #70 - Intermediate
# Wildcard Character Matching
# Objective: Match strings using '?' and '*' with Dynamic Programming.

"""
Match a string against a wildcard pattern containing '?' and '*'.
Demonstrates dynamic programming for complex string matching.
Useful for pattern matching, filters, and glob-like systems.
"""

def wildcard_match(text: str, pattern: str) -> bool:
    """Return True if text matches the wildcard pattern."""
    n = len(text)
    m = len(pattern)

    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True                 # empty text matches empty pattern

    # handle patterns starting with '*'
    for j in range(1, m + 1):
        if pattern[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[j - 1] == text[i - 1] or pattern[j - 1] == "?":
                dp[i][j] = dp[i - 1][j - 1]      # exact or single-char match
            elif pattern[j - 1] == "*":
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                # '*' matches empty or one/more characters

    return dp[n][m]


if __name__ == "__main__":
    text = input("Enter text: ").strip()
    pattern = input("Enter pattern (? and * supported): ").strip()

    result = wildcard_match(text, pattern)
    print(f"Match result: {result}")

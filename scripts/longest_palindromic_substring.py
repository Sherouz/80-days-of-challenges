# Challenge #73 - Intermediate
# Longest Palindromic Substring
# Objective: Find the longest palindromic substring in O(n^2).

"""
Find the longest palindromic substring within a given string.
Demonstrates expand-around-center technique for efficient palindrome detection.
Useful for mastering string traversal and boundary control.
"""

def longest_palindrome(s: str) -> str:
    """Return the longest palindromic substring in s."""
    if not s:
        return ""

    start = 0               # start index of best palindrome
    max_len = 1             # length of best palindrome

    for i in range(len(s)):
        # check odd-length palindromes (single center)
        left = right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            curr_len = right - left + 1
            if curr_len > max_len:
                start = left
                max_len = curr_len
            left -= 1
            right += 1

        # check even-length palindromes (double center)
        left = i
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            curr_len = right - left + 1
            if curr_len > max_len:
                start = left
                max_len = curr_len
            left -= 1
            right += 1

    return s[start:start + max_len]


if __name__ == "__main__":
    text = input("Enter a string: ").strip()
    result = longest_palindrome(text)

    print(f"Longest palindromic substring: {result}")
    print(f"Length: {len(result)}")

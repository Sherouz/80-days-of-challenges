# Challenge #32 - Beginner
# Sort by number of vowels
# Objective: Practice list sorting with custom key functions and string analysis

"""
Given a list of fruit names, sort them by the number of vowels (a, e, i, o, u).
Words with fewer vowels should come first.
"""

def count_vowels(word: str) -> int:
    """
    Return the number of vowels in the given word (case-insensitive).
    """
    vowels = "aeiou"
    return sum(1 for char in word.lower() if char in vowels)


def sort_by_vowel_count(words: list[str]) -> list[str]:
    """
    Return a new list of words sorted by number of vowels.
    """
    return sorted(words, key=count_vowels)


# Example usage
if __name__ == "__main__":
    fruits = ["Apple", "Banana", "Watermelon", "Cherry", "Melon", "Strawberry", "Orange", "Kiwi", "Mango"]
    sorted_fruits = sort_by_vowel_count(fruits)
    print(f"\n🔤 Sorted by vowel count: {sorted_fruits}\n")

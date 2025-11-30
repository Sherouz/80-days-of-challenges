# Challenge #50 - Intermediate
# Grouping Anagrams
# Objective: Practice dictionaries, string normalization, grouping, and basic algorithmic thinking.

"""
Group words that are anagrams of each other.
Two words are anagrams if they contain the same characters
with the same frequency, but in different order.
"""

from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Group words that are anagrams of each other.
    
    Uses a dictionary where the key is the sorted word
    (normalized form), and the value is a list of matching words.
    
    Returns a list of groups, each group containing anagram words.
    """
    groups = defaultdict(list)

    for word in words:
        key = "".join(sorted(word))  # normalized form
        groups[key].append(word)

    return list(groups.values())


# Main program
print("Enter words separated by spaces:")
input_words = input("> ").strip().split()

if not input_words:
    print("No words entered. Exiting.")
else:
    grouped = group_anagrams(input_words)
    print("\nGrouped anagrams:")
    for group in grouped:
        print(group)

# Challenge #49 - Intermediate
# Playlist shuffler simulation
# Objective: Practice list manipulation, randomization, and preserving original data

"""
Simulate shuffling a music playlist.
The program maintains the original playlist and generates a shuffled version
using a Fisher-Yates shuffle to ensure uniform randomness.
"""

import random

def shuffle_playlist(playlist: list) -> list:
    """
    Return a new shuffled playlist using Fisher-Yates algorithm.
    Does not modify the original playlist.
    """
    shuffled = playlist.copy()  # Copy to avoid mutating original playlist
    n = len(shuffled)
    
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)  # Pick a random index from 0 to i
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]  # Swap
    return shuffled

# Example playlist
my_playlist = [
    "Song A - Artist 1",
    "Song B - Artist 2",
    "Song C - Artist 3",
    "Song D - Artist 4",
    "Song E - Artist 5"
]

# Shuffle and print
shuffled_version = shuffle_playlist(my_playlist)
print("Original Playlist:", my_playlist)
print("Shuffled Playlist:", shuffled_version)


# Challenge #28 - Beginner-Intermediate
# Bubble Sort Algorithm
# Objective: Learn how basic sorting algorithms work using nested loops.

"""
Sorts a list of numbers in ascending order using the Bubble Sort algorithm.  
Compares adjacent elements and swaps them if out of order.  
Demonstrates nested loops and step-by-step sorting logic in Python.
"""

def bubble_sort(numbers):
    """
    Sorts a list of numbers using the Bubble Sort algorithm.
    """
    n = len(numbers)
    for i in range(n):
        swapped = False  # Track if any swap happened in this pass
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap the elements
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
        
    return numbers


# Example tests
print(bubble_sort([5, 1, 4, 2, 8]))   # -> [1, 2, 4, 5, 8]
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # -> [11, 12, 22, 25, 34, 64, 90]
print(bubble_sort([3, 2, 1]))  # -> [1, 2, 3]

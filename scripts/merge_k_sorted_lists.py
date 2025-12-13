# Challenge #63 - Intermediate
# Merge K Sorted Lists
# Objective: Merge multiple sorted lists efficiently using a min-heap.

"""
Merge k sorted lists into one sorted list using a min-heap.
Demonstrates priority queues and efficient multi-list merging.
Useful for handling sorted streams and scalable data merging.
"""

import heapq


def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    """
    Merge k sorted lists into a single sorted list.
    Uses a min-heap to always extract the smallest available element.
    """
    heap = []                       # min-heap to track next smallest elements
    result = []                     # final merged output

    # initialize heap with first element of each list
    for i, lst in enumerate(lists):
        if lst:                     # skip empty lists
            heapq.heappush(heap, (lst[0], i, 0))
            # (value, list_index, element_index)

    while heap:
        val, list_i, elem_i = heapq.heappop(heap)
        result.append(val)          # append smallest value to result

        next_i = elem_i + 1
        if next_i < len(lists[list_i]):
            next_val = lists[list_i][next_i]
            heapq.heappush(heap, (next_val, list_i, next_i))
            # push next element from same list

    return result


if __name__ == "__main__":
    raw = input("Enter sorted lists (comma-separated, space-separated numbers): ").strip()

    if raw == "":
        print("No input provided.")
    else:
        lists = []
        for part in raw.split(","):
            nums = list(map(int, part.strip().split()))
            lists.append(nums)

        merged = merge_k_sorted_lists(lists)
        print(f"Merged list: {merged}")

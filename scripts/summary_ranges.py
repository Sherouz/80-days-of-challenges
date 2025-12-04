# Challenge #54 - Intermediate
# Summary Ranges
# Objective: Convert a sorted list of integers into summarized string ranges.

"""
Given a sorted list of unique integers, return a list of strings
summarizing consecutive ranges.
"""

def summary_ranges(nums: list[int]) -> list[str]:
    """
    Return a list of summarized ranges from a sorted list of unique integers.
    Consecutive sequences are collapsed into 'start->end',
    and isolated numbers are returned as single values.
    """
    if not nums:
        return []

    result = []
    start = nums[0]    # beginning of current range

    for i in range(1, len(nums)):
        # If current number is not consecutive, close the previous range
        if nums[i] != nums[i - 1] + 1:
            end = nums[i - 1]
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            start = nums[i]    # start a new range

    # Handle the final range
    end = nums[-1]
    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}->{end}")

    return result


# Main program
raw = input("Enter sorted unique integers (space-separated): ").strip()

if raw == "":
    print("No input provided. Exiting.")
else:
    nums = list(map(int, raw.split()))
    output = summary_ranges(nums)
    print("Summary ranges:", output)

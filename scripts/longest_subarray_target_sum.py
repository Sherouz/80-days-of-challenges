# Challenge #62 - Intermediate
# Longest Subarray with Target Sum
# Objective: Use prefix-sum + hashmap to find the longest contiguous subarray summing to target.

"""
Find the longest continuous subarray whose sum equals the given target.
Uses a hashmap to store the earliest index of each prefix sum for O(n) performance.
Useful for problems involving subarray sums and prefix-sum tricks.
"""

def longest_subarray_with_target(nums: list[int], target: int) -> tuple:
    """
    Return (length, start_idx, end_idx) of the longest subarray with sum == target.
    If no such subarray exists, returns (0, -1, -1).
    """

    # prefix sum -> earliest index (sum zero before start)
    prefix_index = {0: -1}
    prefix = 0         # running prefix sum
    best_len = 0       # best length found so far
    best_start = -1    # start index of best subarray
    best_end = -1      # end index (inclusive) of best subarray

    for i, val in enumerate(nums):
        prefix += val             # update running sum with current value

        # If we've never seen this prefix before, record its earliest index
        if prefix not in prefix_index:
            prefix_index[prefix] = i

        # Check if there's a prefix that makes [j+1 .. i] sum == target
        need = prefix - target
        if need in prefix_index:
            start_idx = prefix_index[need] + 1
            curr_len = i - prefix_index[need]
            if curr_len > best_len:           # update best if longer found
                best_len = curr_len
                best_start = start_idx
                best_end = i

    return best_len, best_start, best_end


# Example usage
if __name__ == "__main__":
    # read input list and target from user
    raw = input("Enter numbers (space-separated): ").strip()
    if raw == "":
        print("No numbers provided.")         # require numbers
    else:
        nums = list(map(int, raw.split()))   # parse ints

        t_raw = input("Enter target sum: ").strip()
        if t_raw == "":
            print("No target provided.")    # require target
        else:
            target = int(t_raw)            # parse target

            # compute
            length, s, e = longest_subarray_with_target(nums, target)   
            if length == 0:
                print(f"No subarray sums to {target}.")
            else:
                # extract subarray
                sub = nums[s:e+1]
                print(f"Longest length: {length}")
                print(f"Subarray (indices {s}..{e}): {sub}")

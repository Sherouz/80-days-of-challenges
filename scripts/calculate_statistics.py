# Challenge #14 - Beginner/Intermediate
# Calculate full statistics (max, min, sum, mean, range)
# Objective: Practice built-in functions, tuple unpacking, and basic error handling

"""
Calculate and display basic statistics from a list of numbers.
Uses built-in functions to find max, min, sum, mean, and range.
Handles empty lists safely with simple validation.
Rounds the mean for cleaner, readable results.
Great for practicing core Python data handling skills.
"""

mixed_numbers = [15, -2, 8, 0, 23, -0.1, 4.8, 7, 7, 2.5, 3.1, 3, 0.5, 19, 3]

def calculate_full_statistics(data):
    """
    Safely calculate basic statistics from a list of numbers.
    Returns a tuple: (max, min, sum, mean, range)
    """
    # 1. Check for empty list (to avoid division by zero)
    if not data:
        return None, None, 0, None, None

    # 2. Basic calculations using built-in functions
    max_val = max(data)
    min_val = min(data)
    total = sum(data)
    mean = round(total / len(data), 2)  # Rounded mean
    data_range = max_val - min_val

    # 3. Return all results as a tuple
    return max_val, min_val, total, mean, data_range


# Function call
max_val, min_val, total, mean, data_range = calculate_full_statistics(mixed_numbers)

# Nicely formatted output
print("\n📊 Full Statistics Report:")
print(f"   📈 Maximum: {max_val}")
print(f"   📉 Minimum: {min_val}")
print(f"   ➕ Sum: {total}")
print(f"   ⚖️  Mean: {mean}")
print(f"   🔢 Range: {data_range}\n")

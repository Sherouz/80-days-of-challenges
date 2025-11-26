# Challenge #46 - Intermediate
# Simple Moving Average Calculator
# Calculates the moving average for a given data series and window size.

"""
This script provides a function to compute the Simple Moving Average (SMA)
for a list of numbers with a specified window size. It demonstrates a basic
sliding window algorithm suitable for intermediate-level algorithm practice.
"""

def calculate_moving_average(data: list[int], window_size: int) -> list[float]:
    """
    Calculate simple moving average (SMA) for a given data list and window size.
    Returns a list of floats representing the SMA values.
    """
    if window_size <= 0 or window_size > len(data):
        return []  # invalid window, return empty list

    moving_averages = []
    window_sum = sum(data[:window_size])  # initial sum for the first window
    moving_averages.append(window_sum / window_size)

    # Slide the window across the data
    for i in range(window_size, len(data)):
        window_sum = window_sum - data[i - window_size] + data[i]
        moving_averages.append(window_sum / window_size)

    return moving_averages


# Main program
input_data = list(map(int, input("Enter the data series (space-separated): ").split()))
window_size = int(input("Enter the window size: "))
result = calculate_moving_average(input_data, window_size)
print("Moving Average:", result)

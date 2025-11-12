# Challenge #32 - Beginner
# Temperature converter: Fahrenheit ↔ Celsius
# Objective: Practice user input, arithmetic operations, and conditional logic

"""
Convert temperature between Fahrenheit and Celsius.
The user chooses the conversion direction and provides a value.
Demonstrates use of arithmetic expressions, conditionals, and formatted output.
"""

def convert_temperature(value: float, to_scale: str) -> float:
    """
    Convert temperature between Fahrenheit and Celsius.
    to_scale must be either 'C' or 'F'.
    """
    if to_scale.upper() == 'C':
        # Convert Fahrenheit to Celsius
        return (value - 32) * 5 / 9
    elif to_scale.upper() == 'F':
        # Convert Celsius to Fahrenheit
        return (value * 9 / 5) + 32
    else:
        raise ValueError("Scale must be 'C' or 'F'.")


# Example interactive test
print("\n🌡️ Temperature Converter")
scale = input("Convert to (C/F): ").strip().upper()
temp = float(input("Enter temperature value: "))

result = convert_temperature(temp, scale)
unit = "°C" if scale == "C" else "°F"
print(f"Converted temperature: {result:.2f}{unit}")

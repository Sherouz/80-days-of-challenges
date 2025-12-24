# Challenge #74 - Intermediate
# Validate IPv4 Address
# Objective: Check whether a string is a valid IPv4 address.

"""
Validate an IPv4 address string.
Demonstrates string parsing, numeric validation, and edge-case handling.
Useful for networking, backend validation, and input sanitization.
"""

def is_valid_ipv4(ip: str) -> bool:
    """Return True if the given string is a valid IPv4 address."""
    parts = ip.split(".")              # split address into parts

    if len(parts) != 4:
        return False                   # IPv4 must have exactly 4 parts

    for part in parts:
        if part == "":
            return False               # empty segment is invalid

        if not part.isdigit():
            return False               # must contain digits only

        if len(part) > 1 and part[0] == "0":
            return False               # no leading zeros allowed

        value = int(part)
        if value < 0 or value > 255:
            return False               # each part must be in range 0–255

    return True


if __name__ == "__main__":
    ip = input("Enter an IPv4 address: ").strip()
    result = is_valid_ipv4(ip)

    print(f"Is valid IPv4: {result}")

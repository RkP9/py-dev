"""
Checks whether a given integer is a palindrome
using mathematical operations only.

Palindrome reads the same forward and backward.
Examples:
- 121  -> True
- -121 -> False
- 10   -> False

"""

def is_palindrome(x: int) -> bool:

    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0

    # Reverse only half of the number
    while x > reversed_half:
        digit = x % 10
        reversed_half = reversed_half * 10 + digit
        x //= 10

    # For even digit count: x == reversed_half (e.g., 1221)
    # For odd digit count:  x == reversed_half // 10 (e.g., 121)
    return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    # Example test cases
    test_cases = [121, -121, 10, 0, 1221, 12321]

    for num in test_cases:
        print(f"{num} -> {is_palindrome(num)}")

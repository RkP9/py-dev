def is_valid_parentheses(s: str) -> bool:
    """
    Determine if the input string has valid parentheses.

    A string is valid if:
    - Open brackets are closed by the same type of brackets
    - Open brackets are closed in the correct order

    Args:
        s (str): Input string containing brackets

    Returns:
        bool: True if valid, False otherwise
    """

    bracket_map = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    stack = []

    for char in s:
        if char in bracket_map:
            top = stack.pop() if stack else "#"
            if bracket_map[char] != top:
                return False
        else:
            stack.append(char)

    return len(stack) == 0


# testing 123 hehe
if __name__ == "__main__":
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "",
        "("
    ]

    for case in test_cases:
        print(f"{case}: {is_valid_parentheses(case)}")

class Solution:
    """
    Convert a Roman numeral string into an integer.

    Example:
    Input: "MCMXCIV"
    Output: 1994
    """

    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to integer values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0

        for i in range(len(s)):
            # If the current value is smaller than the next value,
            # subtract it (subtractive notation like IV, IX, etc.)
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]
            else:
                total += roman_values[s[i]]

        return total
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))      # 3
    print(sol.romanToInt("IV"))       # 4
    print(sol.romanToInt("MCMXCIV"))  # 1994
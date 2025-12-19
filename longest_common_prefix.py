
from typing import List

class Solution:
    """
    Find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string.

    Example:
    Input: ["flower", "flow", "flight"]
    Output: "fl"
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: empty list
        if not strs:
            return ""

        prefix = ""
        first_word = strs[0]

        for i in range(len(first_word)):
            char = first_word[i]

            # Compare this character with the same position in other strings
            for word in strs[1:]:
                if i == len(word) or word[i] != char:
                    return prefix

            prefix += char

        return prefix
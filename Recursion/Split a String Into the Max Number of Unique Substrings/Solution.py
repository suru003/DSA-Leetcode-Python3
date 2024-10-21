"""
Link: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
Time Complexity: O(2^n)
Space Complexity: O(n)
"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        words = set()

        def recurse(index):
            maxi = 0
            for i in range(index + 1, len(s) + 1):
                temp_word = s[index:i]
                if temp_word not in words:
                    words.add(temp_word)
                    maxi = max(maxi, 1 + recurse(i))
                    words.remove(temp_word)

            return maxi

        return recurse(0)

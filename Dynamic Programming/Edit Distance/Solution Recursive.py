"""
Link: https://leetcode.com/problems/edit-distance/
Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""

from math import inf

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def recurse(ind1, ind2):
            if ind2 == len(word2):
                return len(word1) - ind1

            if ind1 == len(word1):
                return len(word2) - ind2

            if (ind1, ind2) in dp:
                return dp[(ind1, ind2)]

            min_distance = inf

            if word1[ind1] == word2[ind2]:
                min_distance = recurse(ind1 + 1, ind2 + 1)
            else:
                min_distance = min(min_distance, recurse(ind1, ind2 + 1) + 1)
                min_distance = min(min_distance, recurse(ind1 + 1, ind2 + 1) + 1)
                min_distance = min(min_distance, recurse(ind1 + 1, ind2) + 1)

            dp[(ind1, ind2)] = min_distance
            return min_distance

        return recurse(0, 0)

"""
Link: https://leetcode.com/problems/longest-square-streak-in-an-array/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
from math import sqrt
import collections


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        ans = -1
        for x in sorted(nums):
            dic[x] = max(1, dic[x])
            sqt = int(sqrt(x))
            if sqt == sqrt(x) and dic[sqt]:
                dic[x] = max(dic[x], dic[sqt] + 1)
            ans = max(ans, dic[x] if dic[x] > 1 else -1)

        return ans


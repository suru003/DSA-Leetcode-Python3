'''
Link: https://leetcode.com/problems/subsets/
Time Complexity: O(2^n)
Space Complexity: O(2^n)
'''
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recurse(i, curr):
            if i >= len(nums):
                ans.append(curr)
            else:
                recurse(i + 1, curr)
                recurse(i + 1, curr + [nums[i]])

        recurse(0, [])
        return ans

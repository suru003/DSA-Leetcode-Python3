"""
Link: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = {}
        maxi = 0
        for val in nums:
            maxi = maxi | val

        def recurse(index, current):
            if (index, current) in dp:
                return dp[(index, current)]

            if index == len(nums):
                return maxi == current

            # ignore
            op1 = recurse(index + 1, current)
            # use it
            op2 = recurse(index + 1, current | nums[index])

            dp[(index, current)] = op1 + op2
            return op1 + op2

        answer = recurse(0, 0)
        return answer

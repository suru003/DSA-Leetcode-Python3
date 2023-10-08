'''
Link: https://leetcode.com/problems/running-sum-of-1d-array/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = [nums[0]]

        for index in range(1, len(nums)):
            sums.append(sums[-1] + nums[index])

        return sums

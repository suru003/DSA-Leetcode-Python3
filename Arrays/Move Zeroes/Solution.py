'''
Link: https://leetcode.com/problems/move-zeroes/
Time Complexity: O(n)
Space Complexity: O(1)
'''
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZeroAt = 0
        for num in nums:
            if num:
                nums[nonZeroAt] = num
                nonZeroAt += 1

        for index in range(nonZeroAt, len(nums)):
            nums[index] = 0

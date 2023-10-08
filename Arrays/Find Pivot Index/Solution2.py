'''
Link: https://leetcode.com/problems/find-pivot-index/
Time Complexity: O(n)
Space Complexity: O(1)
'''
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        remained, left = sum(nums), 0

        for index in range(len(nums)):
            left += nums[index]

            if left == remained:
                return index

            remained -= nums[index]

        return -1

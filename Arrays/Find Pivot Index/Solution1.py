'''
Link: https://leetcode.com/problems/find-pivot-index/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = [nums[0]], [nums[-1]]
        n = len(nums)

        for index in range(1, n):
            leftSum.append(leftSum[-1] + nums[index])
            rightSum.append(rightSum[-1] + nums[-index - 1])

        # Since, rightSum stores sums in the reverse order
        for index in range(n):
            if leftSum[index] == rightSum[-index - 1]:
                return index

        return -1
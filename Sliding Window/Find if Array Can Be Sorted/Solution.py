"""
Link: https://leetcode.com/problems/find-if-array-can-be-sorted/
Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        i, n = 0, len(nums)
        prev_max = 0

        def get_ones(num):
            return str(bin(num)).count('1')

        while i < n:
            window_ones = get_ones(nums[i])
            mini, maxi = nums[i], nums[i]

            j = i + 1

            while j < n and get_ones(nums[j]) == window_ones:
                mini, maxi = min(mini, nums[j]), max(maxi, nums[j])
                j += 1

            if mini < prev_max:
                return False

            prev_max = maxi
            i = j

        return True

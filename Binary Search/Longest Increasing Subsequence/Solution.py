'''
Link: https://leetcode.com/problems/number-of-matching-subsequences/
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''
from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []

        for num in nums:
            index = bisect_left(stack, num)
            if len(stack) == index:
                stack.append(num)
            else:
                stack[index] = num

        return len(stack)

'''
Link: https://leetcode.com/problems/find-the-most-competitive-subsequence/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []

        for i, num in enumerate(nums):
            while stack and stack[-1] > num and k - len(stack) < len(nums) - i:
                stack.pop()

            if len(stack) < k:
                stack.append(num)

        return stack

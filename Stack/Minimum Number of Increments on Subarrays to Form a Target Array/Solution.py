'''
Link: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
Time Complexity: O(n)
Space Complexity: O(1)
'''
from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        total = target[0]

        for index in range(1, len(target)):
            total += max(0, target[index] - target[index - 1])

        return total

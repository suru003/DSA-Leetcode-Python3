'''
Link: https://leetcode.com/problems/merge-intervals/
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []

        for start, end in sorted(intervals):
            if not stack or stack[-1][1] < start:
                stack.append([start, end])
            else:
                stack[-1][1] = max(end, stack[-1][1])

        return stack

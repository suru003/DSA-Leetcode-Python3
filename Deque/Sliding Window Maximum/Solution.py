"""
Link: https://leetcode.com/problems/sliding-window-maximum/description/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        answer = []

        for index, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(index)

            while dq and index - dq[0] >= k:
                dq.popleft()

            if index >= k - 1:
                answer.append(nums[dq[0]])

        return answer

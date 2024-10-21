"""
Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefSum = [0]

        for i in range(len(cardPoints)):
            prefSum.append(cardPoints[i] + prefSum[-1])

        maxPoints = 0
        for i in range(k + 1):
            maxPoints = max(maxPoints, prefSum[i] + (prefSum[-1] - prefSum[-k + i - 1]))

        return maxPoints

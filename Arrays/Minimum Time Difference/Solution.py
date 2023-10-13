'''
Link: https://leetcode.com/problems/minimum-time-difference/
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []

        def getMinutes(point):
            temp = point.split(":")
            return 60 * int(temp[0]) + int(temp[1])

        for point in timePoints:
            minutes.append(getMinutes(point))

        minutes.sort()
        minDiff = float('inf')
        for index in range(1, len(minutes)):
            minDiff = min(minDiff, minutes[index] - minutes[index - 1])

        return min(minDiff, (getMinutes("24:00") - minutes[-1] + minutes[0] - getMinutes("00:00")))

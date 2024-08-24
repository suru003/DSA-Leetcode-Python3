"""
Link: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
n:= len(ranges)
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
from typing import List
import heapq as hq


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        heap = []

        for index, dx in enumerate(ranges):
            if dx == 0:
                continue

            right = min(index + dx, n)
            left = max(0, index - dx)

            hq.heappush(heap, [left, -right])

        count = 0
        cur = 0
        while heap:
            # when a point is unreachable
            if heap[0][0] > cur:
                break

            count += 1
            nex = cur
            # get the next max window
            while heap and cur >= heap[0][0]:
                nex = max(nex, -hq.heappop(heap)[1])

            cur = nex
            # to ignore the next smaller windows
            while heap and cur >= -heap[0][1]:
                hq.heappop(heap)

        if cur < n:
            return -1

        return count

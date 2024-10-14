"""
Link: https://leetcode.com/problems/meeting-rooms-ii/
Link: https://www.lintcode.com/problem/919/
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
from typing import List
from lintcode import (
    Interval,
)

import heapq as hq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        answer, heap = 0, []

        for interval in sorted(intervals, key=lambda x: x.start):
            while heap and interval.start >= heap[0]:
                hq.heappop(heap)
            hq.heappush(heap, interval.end)
            answer = max(answer, len(heap))

        return answer

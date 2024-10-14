"""
Link: https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
from typing import List
import heapq as hq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        empty = [val for val in range(10 ** 5)]
        filled = []
        ind_times = [times[ind] + [ind] for ind in range(len(times))]

        for arr, dep, ind in sorted(ind_times):
            while filled and filled[0][0] <= arr:
                empty_chair = hq.heappop(filled)[1]
                hq.heappush(empty, empty_chair)

            if ind == targetFriend:
                return hq.heappop(empty)

            filled_chair = hq.heappop(empty)
            hq.heappush(filled, [dep, filled_chair])

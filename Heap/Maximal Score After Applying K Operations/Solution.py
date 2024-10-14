"""
Link: https://leetcode.com/problems/maximal-score-after-applying-k-operations/
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
import heapq as hq
from typing import List
import math


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            hq.heappush(heap, -num)

        answer = 0

        while k:
            num = -hq.heappop(heap)
            answer += num
            num = math.ceil(num / 3)
            hq.heappush(heap, -num)
            k -= 1

        return answer

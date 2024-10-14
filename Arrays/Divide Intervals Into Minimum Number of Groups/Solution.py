# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
from typing import List
from collections import defaultdict

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals_sorted = sorted(intervals)
        dic = defaultdict(int)

        for start, end in intervals_sorted:
            dic[start] += 1
            dic[end + 1] -= 1

        cur, maxi = 0, 0
        for key in sorted(dic.keys()):
            cur += dic[key]
            maxi = max(maxi, cur)

        return maxi

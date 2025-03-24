"""
Link: https://leetcode.com/problems/zero-array-transformation-ii/
Time Complexity: O((n+m)∗log(m))
Space Complexity: O(n)
"""
from typing import List
from collections import defaultdict

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(not num for num in nums):
            return 0

        n, m = len(nums), len(queries)
        left, right = 0, m - 1

        def is_valid(x):
            offsets = defaultdict(int)
            for a, b, val in queries[:x + 1]:
                offsets[a] -= val
                offsets[b + 1] += val

            offset = 0
            for ind, val in enumerate(nums):
                offset += offsets[ind]
                if val + offset > 0:
                    return False

            return True

        answer = -2
        while left <= right:
            mid = (left + right) >> 1
            if is_valid(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer + 1

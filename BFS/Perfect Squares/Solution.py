"""
Link: https://leetcode.com/problems/perfect-squares/
Time Complexity: O(n*sqrt(n))
Space Complexity: O(n)
"""
from collections import deque
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        dq = deque()
        visited = set()

        for val in range(1, int(sqrt(n)) + 1):
            to_add = (val * val)
            dq.append([1, to_add])
            visited.add(to_add)

        while dq:
            steps, val = dq.popleft()
            if val == n:
                return steps

            for nex in range(1, int(sqrt(n - val)) + 1):
                to_add = val + (nex * nex)
                if to_add not in visited:
                    dq.append([steps + 1, to_add])
                    visited.add(to_add)

        return 0
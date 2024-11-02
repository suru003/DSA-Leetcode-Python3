"""
Link: https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/
Time Complexity: O(nm)
Space Complexity: O(nm)
"""
from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = {}
        m, n = len(grid), len(grid[0])
        adj = [[-1, 1], [0, 1], [1, 1]]

        def recurse(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            nexts = 0
            for a, b in adj:
                if 0 <= a + i < m and 0 <= b + j < n and grid[a + i][b + j] > grid[i][j]:
                    nexts = max(nexts, 1 + recurse(a + i, b + j))

            dp[(i, j)] = nexts
            return dp[(i, j)]

        ans = 0

        for i in range(m):
            ans = max(recurse(i, 0), ans)

        return ans

"""
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
Time Complexity: O(mn)
Space Complexity: O(mn)
"""
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        canReach = [[0 for _ in range(n)] for _ in range(m)]
        adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dq = deque()
        visited = set()

        def bfs():
            while dq:
                ci, cj = dq.popleft()
                canReach[ci][cj] += 1

                for di, dj in adj:
                    ai, aj = ci + di, cj + dj

                    if (ai, aj) not in visited \
                            and 0 <= ai < m and 0 <= aj < n \
                            and heights[ai][aj] >= heights[ci][cj]:
                        visited.add((ai, aj))
                        dq.append((ai, aj))

        # from Pacific
        # top row
        for i in range(n):
            visited.add((0, i))
            dq.append((0, i))
        # left col
        for i in range(1, m):
            visited.add((i, 0))
            dq.append((i, 0))

        bfs()
        visited = set()

        # from Atlantic
        # bottom row
        for i in range(n):
            visited.add((m - 1, i))
            dq.append((m - 1, i))
        # right col
        for i in range(m - 1):
            visited.add((i, n - 1))
            dq.append((i, n - 1))

        bfs()

        return [[i, j] for i in range(m) for j in range(n) if canReach[i][j] > 1]

"""
Link: https://leetcode.com/problems/rotting-oranges/
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
from typing import List
from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dq = deque()
        m, n = len(grid), len(grid[0])
        not_rotten = 0
        visited = set()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    dq.append([row, col])
                    visited.add((row, col))
                elif grid[row][col] == 1:
                    not_rotten += 1

        dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        timer = 0

        while dq:
            level = len(dq)

            while level:
                x, y = dq.popleft()

                for dx, dy in dxy:
                    ax, ay = x + dx, y + dy

                    if 0 <= ax < m and 0 <= ay < n \
                            and (ax, ay) not in visited \
                            and grid[ax][ay] == 1:
                        dq.append([ax, ay])
                        visited.add((ax, ay))
                        not_rotten -= 1

                level -= 1

            timer += 1

        return -1 if not_rotten else max(0, timer - 1)

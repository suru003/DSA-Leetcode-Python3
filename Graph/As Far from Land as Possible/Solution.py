'''
Link: https://leetcode.com/problems/as-far-from-land-as-possible/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j]])

        if len(q) == m * n or len(q) == 0:
            return -1

        distance = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xi, yj = x + i, y + j

                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                        q.append((xi, yj))
                        grid[xi][yj] = 1

            distance += 1

        return distance - 1

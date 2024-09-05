"""
Link: https://leetcode.com/problems/detect-cycles-in-2d-grid/
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""
from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def dfs(cx, cy, px, py):
            for dx, dy in dxy:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < m and 0 <= ny < n \
                        and (not (nx == px and ny == py)) \
                        and grid[cx][cy] == grid[nx][ny]:
                    if (nx, ny) in visited:
                        return True

                    visited.add((nx, ny))
                    if dfs(nx, ny, cx, cy):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    visited.add((i, j))
                    if dfs(i, j, -1, -1):
                        return True

        return False

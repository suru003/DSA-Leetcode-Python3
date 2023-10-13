'''
Link: https://leetcode.com/problems/number-of-islands/
Time Complexity: O(n*m)
Space Complexity: O(n*m)
'''
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]

        def dfs(row, col):
            if 0 <= row < n and 0 <= col < m and grid[row][col] == '1' and not visited[row][col]:
                visited[row][col] = 1
                for a, b in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    dfs(row + a, col + b)

        islands = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1' and not visited[row][col]:
                    dfs(row, col)
                    islands += 1

        return islands

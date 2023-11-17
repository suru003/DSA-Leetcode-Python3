'''
Link: https://leetcode.com/problems/max-area-of-island/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        adjacents = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        answer, m, n = 0, len(grid), len(grid[0])
        visited = set()

        def getArea(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0
            if not grid[row][col]:
                return 0
            if (row, col) in visited:
                return 0

            visited.add((row, col))
            total = 1
            for dx, dy in adjacents:
                total += getArea(row + dx, col + dy)

            return total

        for row in range(m):
            for col in range(n):
                answer = max(answer, getArea(row, col))

        return answer

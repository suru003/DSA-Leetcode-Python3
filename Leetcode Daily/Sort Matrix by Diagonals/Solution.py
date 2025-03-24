"""
Link: https://leetcode.com/problems/sort-matrix-by-diagonals/
Time Complexity: O(m*n)
Space Complexity: O(min(m, n))
"""
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        for row in range(m - 1, -1, -1):
            temp_list = []
            x, y = row, 0
            while x < m and y < n:
                temp_list.append(grid[x][y])
                x, y = x + 1, y + 1

            temp_list.sort(reverse=True)
            index = 0
            x, y = row, 0
            while x < m and y < n:
                grid[x][y] = temp_list[index]
                x, y = x + 1, y + 1
                index += 1

        for col in range(n - 1, 0, -1):
            temp_list = []
            x, y = 0, col
            while x < m and y < n:
                temp_list.append(grid[x][y])
                x, y = x + 1, y + 1

            temp_list.sort()
            index = 0
            x, y = 0, col
            while x < m and y < n:
                grid[x][y] = temp_list[index]
                x, y = x + 1, y + 1
                index += 1

        return grid

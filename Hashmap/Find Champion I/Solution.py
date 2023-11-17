'''
Link: https://leetcode.com/contest/weekly-contest-370/problems/find-champion-i/
Time Complexity: O(n*n)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        loosers = set()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    loosers.add(j)

        for i in range(n):
            if i not in loosers:
                return i

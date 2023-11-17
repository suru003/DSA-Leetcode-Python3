'''
Link: https://leetcode.com/problems/walls-and-gates/
Link: https://www.lintcode.com/problem/663/
Time Complexity: O(rowsXcols)
Space Complexity: O(1)
'''
from typing import List
from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        dq = deque()
        rows, cols = len(rooms), len(rooms[0])
        INF = 2147483647

        for row in range(rows):
            for col in range(cols):
                if not rooms[row][col]:
                    dq.append((row, col, 0))

        adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while dq:
            cur_row, cur_col, dist = dq.popleft()

            for dr, dc in adj:
                nex_row, nex_col = cur_row + dr, cur_col + dc
                if 0 <= nex_row < rows and 0 <= nex_col < cols and rooms[nex_row][nex_col] == INF:
                    rooms[nex_row][nex_col] = dist + 1
                    dq.append((nex_row, nex_col, dist + 1))

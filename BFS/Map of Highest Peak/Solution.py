"""
Link: https://leetcode.com/problems/map-of-highest-peak/
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""
from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dq = deque()
        m, n = len(isWater), len(isWater[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    isWater[i][j] = 0
                    visited.add((i, j))
                    dq.append((i, j))

        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n

        while dq:
            x, y = dq.popleft()
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (dx, dy) not in visited and is_valid(dx, dy):
                    isWater[dx][dy] = isWater[x][y] + 1
                    visited.add((dx, dy))
                    dq.append((dx, dy))

        return isWater

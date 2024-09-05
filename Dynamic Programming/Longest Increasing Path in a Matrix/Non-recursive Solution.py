"""
Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/submissions/1371262542/
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[1] * n for _ in range(m)]

        def dfs(row, col):
            if dp[row][col] != 1:
                return dp[row][col]

            maxi = 0
            for ai, aj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                a_row, a_col = ai + row, aj + col

                if 0 <= a_row < m and 0 <= a_col < n and matrix[a_row][a_col] > matrix[row][col]:
                    maxi = max(maxi, 1 + dfs(a_row, a_col))

            dp[row][col] = maxi
            return maxi

        for row in range(m):
            for col in range(n):
                if dp[row][col] == 1:
                    dp[row][col] = dfs(row, col)

        return max(max(row) for row in dp) + 1

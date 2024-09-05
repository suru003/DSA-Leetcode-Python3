"""
Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/submissions/1371262542/
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp: dict[int] = {}
        dxy: List[int] = [0, -1, 0, 1, 0]
        m, n = len(matrix), len(matrix[0])

        def recurse(i: int, j: int) -> int:
            if (i, j) in dp:
                return dp[(i, j)]

            longest: int = 1

            for index in range(len(dxy) - 1):
                dx, dy = dxy[index], dxy[index + 1]
                next_i, next_j = i + dx, j + dy
                if (0 <= next_i < m and 0 <= next_j < n) and matrix[next_i][next_j] > matrix[i][j]:
                    longest = max(longest, 1 + recurse(next_i, next_j))

            dp[(i, j)] = longest
            return longest

        answer: int = 0

        for row in range(m):
            for col in range(n):
                answer = max(answer, recurse(row, col))

        return answer
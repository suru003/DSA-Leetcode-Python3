'''
Link: https://leetcode.com/problems/word-search/
Time Complexity: O(mn)
Space Complexity: O(mn)
'''
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, end = len(board), len(board[0]), len(word) - 1
        adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def dfs(row, col, index):
            if not (0 <= row < m and 0 <= col < n):
                return False

            if end == index and word[index] == board[row][col]:
                return True

            if word[index] != board[row][col]:
                return False

            found = False
            for di, dj in adj:
                ai, aj = row + di, col + dj

                if (ai, aj) not in visited:
                    visited.add((ai, aj))
                    found = found or dfs(ai, aj, index + 1)
                    visited.remove((ai, aj))

            return found

        for r in range(m):
            for c in range(n):
                visited.add((r, c))
                if dfs(r, c, 0):
                    return True
                visited.remove((r, c))

        return False

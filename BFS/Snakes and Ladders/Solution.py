"""
Link: https://leetcode.com/problems/snakes-and-ladders/
Time Complexity: O(n * n)
Space Complexity: O(n * n)
"""
from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        graph, visited = {}, set([1])

        reverse = False
        index, limit = 1, n * n
        for row in board[::-1]:
            if reverse:
                row = row[::-1]

            for val in row:
                if val > 0:
                    graph[index] = val
                index += 1

            reverse = not reverse

        if not graph:
            return limit // 6 + (limit % 6 > 0)

        dq = deque()
        dq.append([1, 0])

        while dq:
            current, move = dq.popleft()
            visited.add(current)

            if current == limit:
                return move

            for next_move in range(current + 1, min(limit, current + 6) + 1):
                shift_to = graph.get(next_move, next_move)
                if shift_to not in visited:
                    dq.append([shift_to, move + 1])

        return -1

"""
Link: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
Time Complexity: O(nd)
Space Complexity: O(nd)
"""
from functools import cache
from math import inf
from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        @cache
        def recurse(index, day):
            if n - index < day:
                return -1

            if day == 1:
                return max(jobDifficulty[index:])

            mini = inf
            max_so_far = jobDifficulty[index]

            for next_index in range(index, n):
                max_so_far = max(max_so_far, jobDifficulty[next_index])
                next_answer = recurse(next_index + 1, day - 1)

                if next_answer != -1:
                    mini = min(mini, max_so_far + next_answer)

            return -1 if mini == inf else mini

        return recurse(0, d)


from typing import List
from collections import deque

"""
[[1, 1, 1, 1],
 [0, 0, 0, 1],
 [1, 1, 1, 1]]
"""


def shortestCellPath(grid: List[List[int]], sr: int, sc: int, tr: int, tc: int) -> int:
    dq = deque()
    visited = set()
    dq.append((sr, sc, 0))  # [(0, 0, 0)]
    visited.add((sr, sc))

    dxy = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    while dq:
        cur_x, cur_y, cur_d = dq.popleft()  # 0, 1, 1

        if cur_x == tr and cur_y == tc:
            return cur_d

        for dx, dy in dxy:
            nex_x, nex_y = cur_x + dx, cur_y + dy
            if (nex_x, nex_y) not in visited and is_valid(nex_x, nex_y) \
                    and grid[nex_x][nex_y]:
                visited.add((nex_x, nex_y))
                dq.append((nex_x, nex_y, cur_d + 1))

    return -1


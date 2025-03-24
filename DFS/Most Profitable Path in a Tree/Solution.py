"""
Link: https://leetcode.com/problems/most-profitable-path-in-a-tree/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        nodes = len(amount)
        bobPath = [-1] * nodes
        path = [bob]

        def fillBobPath(current, parent):
            if current == 0:
                return True

            for nbr in graph[current]:
                if nbr != parent:
                    path.append(nbr)
                    if fillBobPath(nbr, current):
                        return True
                    path.pop()

            return False

        fillBobPath(bob, -1)
        for index, val in enumerate(path):
            bobPath[val] = index

        def alicePath(current, parent, current_time):
            score = 0

            if bobPath[current] > current_time \
                    or bobPath[current] == -1:
                score = amount[current]
            elif bobPath[current] == current_time:
                score = amount[current] // 2

            local_max = -inf
            went_in = False
            for nbr in graph[current]:
                if nbr != parent:
                    went_in = True
                    local_max = max(local_max, score + alicePath(nbr, current, current_time + 1))

            return local_max if went_in else score

        return alicePath(0, -1, 0)

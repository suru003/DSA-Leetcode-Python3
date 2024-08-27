"""
Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parents: List[int] = [i for i in range(n)]
        self.N: int = n

    def find(self, cur: int) -> int:
        if self.parents[cur] != cur:
            self.parents[cur] = self.find(self.parents[cur])

        return self.parents[cur]

    def union(self, index_a: int, index_b: int) -> None:
        parent_a, parent_b = self.find(index_a), self.find(index_b)
        if parent_a != parent_b:
            self.parents[parent_a] = parent_b


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu = DSU(n)
        spare = 0

        for a, b in connections:
            par_a, par_b = dsu.find(a), dsu.find(b)
            if par_a != par_b:
                dsu.union(par_a, par_b)
            else:
                spare += 1

        required_cables = len(set([dsu.find(a) for a in range(n)])) - 1
        return -1 if spare < required_cables else required_cables

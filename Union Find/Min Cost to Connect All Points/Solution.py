"""
Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges: List[int] = []
        n: int = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                point_a, point_b = points[i], points[j]
                edges.append([abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1]), \
                              i, j])

        edges.sort()
        dsu: object = DSU(n)

        added_edges: int = 0
        total_cost: int = 0

        for cost, a, b in edges:
            par_a, par_b = dsu.find(a), dsu.find(b)
            if par_a != par_b:
                dsu.union(par_a, par_b)
                total_cost += cost
                added_edges += 1

            if added_edges == n - 1:
                return total_cost

        return total_cost

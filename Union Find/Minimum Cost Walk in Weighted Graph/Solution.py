"""
Link: https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
Time Complexity: O(Q + N)
Space Complexity: O(n)
"""
from typing import List

class DSU:
    def __init__(self, size):
        self.MAX_VAL = 2 ** 20 - 1
        self.parents = [i for i in range(size)]
        self.sizes = [1] * size
        self.min_val = [self.MAX_VAL] * size

    def find_parent(self, current):
        parent = self.parents[current]
        if parent != current:
            self.parents[current] = self.find_parent(parent)

        return self.parents[current]

    def union(self, a, b, edge):
        parent_a, parent_b = self.find_parent(a), self.find_parent(b)

        if parent_a == parent_b:
            self.min_val[parent_a] &= edge
        else:
            if self.sizes[parent_a] < self.sizes[parent_b]:
                self.sizes[parent_b] += self.sizes[parent_a]
                self.parents[parent_a] = parent_b
                self.min_val[parent_b] &= self.min_val[parent_a] & edge
            else:
                self.sizes[parent_a] += self.sizes[parent_b]
                self.parents[parent_b] = parent_a
                self.min_val[parent_a] &= self.min_val[parent_b] & edge


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DSU(n)
        for a, b, weight in edges:
            dsu.union(a, b, weight)

        answer = []
        for a, b in query:
            parent_a, parent_b = dsu.find_parent(a), dsu.find_parent(b)
            if parent_a == parent_b:
                answer.append(dsu.min_val[parent_a])
            else:
                answer.append(-1)

        return answer

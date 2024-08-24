"""
Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List


class DSU:
    def __init__(self, n):
        self.parents = [node for node in range(n + 1)]
        self.sizes = [1 for _ in range(n + 1)]
        self.N = n

    def findParent(self, node):
        parent = self.parents[node]
        if parent != node:
            self.parents[node] = self.findParent(parent)

        return self.parents[node]

    def union(self, a_node, b_node):
        a_parent, b_parent = self.findParent(a_node), self.findParent(b_node)

        if a_parent != b_parent:
            a_sizes, b_sizes = self.sizes[a_parent], self.sizes[b_parent]

            if a_sizes > b_sizes:
                self.parents[b_parent] = a_parent
                self.sizes[a_parent] += self.sizes[b_parent]
            else:
                self.parents[a_parent] = b_parent
                self.sizes[b_parent] += self.sizes[a_parent]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        last_redundant = None
        dsu = DSU(len(edges))

        for a, b in edges:
            parent_a, parent_b = dsu.findParent(a), dsu.findParent(b)
            dsu.union(parent_a, parent_b)
            if parent_a == parent_b:
                last_redundant = [a, b]

        return last_redundant

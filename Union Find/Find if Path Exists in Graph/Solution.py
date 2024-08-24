"""
Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List


class DSU:
    def __init__(self, n):
        self.parents = [node for node in range(n)]
        self.sizes = [1 for _ in range(n)]
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

    def is_valid(self, a_node, b_node):
        a_parent, b_parent = self.findParent(a_node), self.findParent(b_node)
        return a_parent == b_parent


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dsu = DSU(n)

        for a, b in edges:
            dsu.union(a, b)

        return dsu.is_valid(source, destination)

"""
Link: https://leetcode.com/problems/number-of-provinces/description/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List

class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [1 for _ in range(size)]
        self.total_unique = size

    def find_parent(self, current):
        parent = self.parents[current]
        if parent == current:
            return current

        self.parents[current] = self.find_parent(parent)
        return self.parents[current]

    def union(self, a, b):
        parent_a, parent_b = self.find_parent(a), self.find_parent(b)

        if parent_a != parent_b:
            self.total_unique -= 1
            if self.sizes[parent_a] < self.sizes[parent_b]:
                self.sizes[parent_b] += self.sizes[parent_a]
                self.parents[parent_a] = parent_b
            else:
                self.sizes[parent_a] += self.sizes[parent_b]
                self.parents[parent_b] = parent_a


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
                    uf.union(i, j)

        return uf.total_unique

"""
Link: https://leetcode.com/problems/longest-square-streak-in-an-array/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List


class DSU:
    def __init__(self):
        self.parents = {}
        self.sizes = {}

    def add_val(self, val):
        self.parents[val] = val
        self.sizes[val] = 1

    def find_parent(self, val):
        if self.parents[val] == val:
            return val

        self.parents[val] = self.find_parent(self.parents[val])
        return self.parents[val]

    def union(self, a, b):
        parent_a = self.find_parent(a)
        parent_b = self.find_parent(b)

        if parent_a != parent_b:
            if parent_a >= parent_b:
                self.parents[parent_b] = self.parents[parent_a]
                self.sizes[parent_a] += self.sizes[parent_b]
            else:
                self.parents[parent_a] = self.parents[parent_b]
                self.sizes[parent_b] += self.sizes[parent_a]


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dsu = DSU()
        for val in nums:
            dsu.add_val(val)

        for val in nums:
            nex = val ** 2
            dsu.find_parent(val)

            if nex in dsu.parents:
                dsu.union(val, nex)

        answer = max(dsu.sizes.values())
        return -1 if answer == 1 else answer

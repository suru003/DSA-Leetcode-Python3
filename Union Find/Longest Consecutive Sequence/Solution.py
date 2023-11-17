'''
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.sizes = defaultdict(int)

    def find(self, cur):
        if cur not in self.parent:
            self.parent[cur] = cur
            self.sizes[cur] = 1
            return cur

        if self.parent[cur] != cur:
            self.parent[cur] = self.find(self.parent[cur])

        return self.parent[cur]

    def union(self, a, b):
        if b not in self.parent:
            return

        parentA = self.find(a)
        parentB = self.find(b)
        if parentA != parentB:
            if self.sizes[parentA] > self.sizes[parentB]:
                self.parent[parentB] = parentA
                self.sizes[parentA] += self.sizes[parentB]
            else:
                self.parent[parentA] = parentB
                self.sizes[parentB] += self.sizes[parentA]

    def maxi(self):
        return max(self.sizes.values()) if self.sizes else 0


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind()

        for num in nums:
            uf.find(num)
            uf.union(num, num - 1)
            uf.union(num, num + 1)

        return uf.maxi()

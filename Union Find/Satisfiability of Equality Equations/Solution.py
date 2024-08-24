"""
Link: https://leetcode.com/problems/satisfiability-of-equality-equations/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List


class DSU:
    def __init__(self):
        self.parent = {}

    def findParent(self, cur):
        if cur not in self.parent:
            self.parent[cur] = cur

        if self.parent[cur] != cur:
            self.parent[cur] = self.findParent(self.parent[cur])

        return self.parent[cur]

    def union(self, cur_a, cur_b):
        par_a, par_b = self.findParent(cur_a), self.findParent(cur_b)

        if par_a != par_b:
            self.parent[par_b] = par_a


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equals = DSU()

        for equation in equations:
            a, sign, b = equation[0], equation[1], equation[-1]

            if sign == '=':
                par_a, par_b = equals.findParent(a), equals.findParent(b)
                if par_a != par_b:
                    equals.union(par_a, par_b)

        for equation in equations:
            a, sign, b = equation[0], equation[1], equation[-1]
            if sign == '!':
                par_a, par_b = equals.findParent(a), equals.findParent(b)
                if par_a == par_b:
                    return False

        return True

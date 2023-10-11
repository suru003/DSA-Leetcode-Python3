'''
Link: https://leetcode.com/problems/find-the-town-judge/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree, outdegree = [0] * n, [0] * n

        for a, b in trust:
            indegree[b - 1] += 1
            outdegree[a - 1] += 1

        for index in range(n):
            if indegree[index] == n - 1 and outdegree[index] == 0:
                return index + 1

        return -1
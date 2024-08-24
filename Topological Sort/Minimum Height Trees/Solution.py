"""
Link: https://leetcode.com/problems/minimum-height-trees/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
from collections import defaultdict
import copy

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        indegrees = [0] * n
        graph = defaultdict(list)

        for a, b in edges:
            indegrees[a] += 1
            indegrees[b] += 1
            graph[a].append(b)
            graph[b].append(a)

        level = []
        removed = set()

        for node in range(n):
            if indegrees[node] == 1:
                level.append(node)
                removed.add(node)

        while level:
            temp = []

            for node in level:
                for adj in graph[node]:
                    if adj not in removed:
                        indegrees[adj] -= 1
                        if indegrees[adj] == 1:
                            temp.append(adj)
                            removed.add(adj)

            if not temp:
                return level

            level = copy.deepcopy(temp)

        return []

"""
Link: https://leetcode.com/problems/critical-connections-in-a-network/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        entered = [float('inf')] * n
        minimum = [float('inf')] * n
        answer = []
        time = 0

        def dfs(current, parent):
            nonlocal time
            entered[current] = time
            minimum[current] = time
            time += 1

            for child in graph[current]:
                if child != parent:
                    if entered[child] == float('inf'):
                        minimum[current] = min(minimum[current], dfs(child, current))
                    else:
                        minimum[current] = min(minimum[current], minimum[child])

                    if entered[current] < minimum[child]:
                        answer.append([current, child])

            return minimum[current]

        dfs(0, -1)
        return answer

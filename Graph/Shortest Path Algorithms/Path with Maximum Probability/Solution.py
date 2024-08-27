"""
Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
Time Complexity: O(N * E)
Space Complexity: O(N + E)
"""
from typing import List
from collections import defaultdict
import heapq as hq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        graph = defaultdict(list)
        heap = []

        for i in range(len(edges)):
            a, b, prob = edges[i][0], edges[i][1], succProb[i]
            graph[a].append([b, prob])
            graph[b].append([a, prob])

        visited = set([start_node])

        for b, prob in graph[start_node]:
            hq.heappush(heap, [-prob, b])

        while heap:
            prob, node = hq.heappop(heap)
            visited.add(node)

            if node == end_node:
                return -prob

            for adj, adj_prob in graph[node]:
                if adj not in visited:
                    hq.heappush(heap, [prob * adj_prob, adj])

        return 0

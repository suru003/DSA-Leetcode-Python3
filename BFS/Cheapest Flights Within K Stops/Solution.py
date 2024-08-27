'''
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List
from collections import defaultdict, deque


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dq = deque()
        visited = [float('inf')] * n
        graph = defaultdict(list)

        for a, b, cost in flights:
            graph[a].append([b, cost])

        dq.append([src, 0])
        visited[src] = 0

        while k >= 0 and dq:
            next_level = len(dq)

            while next_level:
                cur, cost = dq.popleft()

                for adj, next_cost in graph[cur]:
                    total_cost = cost + next_cost
                    if total_cost < visited[adj]:
                        visited[adj] = total_cost
                        dq.append([adj, total_cost])

                next_level -= 1

            k -= 1

        return -1 if visited[dst] == float('inf') else visited[dst]

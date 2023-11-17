'''
Link: https://leetcode.com/problems/network-delay-time/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List
from collections import defaultdict, deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for a, b, t in times:
            graph[a].append([b, t])

        visitedTime = [float('inf')] * n
        visitedTime[k - 1] = 0

        dq = deque()
        dq.append([k, 0])

        while dq:
            cur, curTime = dq.popleft()

            for adj, time in graph[cur]:
                if visitedTime[adj - 1] > time + curTime:
                    visitedTime[adj - 1] = time + curTime
                    dq.append([adj, curTime + time])

        return max(visitedTime) if max(visitedTime) != float('inf') else -1

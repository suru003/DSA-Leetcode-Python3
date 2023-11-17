'''
Link: https://leetcode.com/contest/weekly-contest-370/problems/find-champion-ii/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegrees = [0] * n

        for a, b in edges:
            indegrees[b] += 1

        winners = []

        for index in range(n):
            if not indegrees[index]:
                winners.append(index)

        return winners[0] if len(winners) == 1 else -1

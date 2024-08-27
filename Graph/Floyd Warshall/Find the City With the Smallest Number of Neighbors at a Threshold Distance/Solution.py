"""
Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance_matrix = [[float('inf')] * n for _ in range(n)]

        for a, b, weight in edges:
            distance_matrix[a][b] = distance_matrix[b][a] = weight

        for i in range(n):
            distance_matrix[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance_matrix[i][j] = min(distance_matrix[i][j],
                                                distance_matrix[i][k] + distance_matrix[k][j])

        mini, node = n, 0
        for i in range(n):
            count = 0
            for j in range(n):
                if distance_matrix[i][j] <= distanceThreshold:
                    count += 1

            if count <= mini:
                mini = count
                node = i

        return node

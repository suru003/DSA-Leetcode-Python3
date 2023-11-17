'''
Link: https://leetcode.com/problems/spiral-matrix/
Time Complexity: O(nXm)
Space Complexity: O(nXm)
'''
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        total = m * n
        top, left, bottom, right = 0, 0, m - 1, n - 1
        answer = []

        while len(answer) < total:
            # top
            if left <= right:
                for a in range(left, right + 1):
                    answer.append(matrix[top][a])
                top += 1

            # right
            if top <= bottom:
                for a in range(top, bottom + 1):
                    answer.append(matrix[a][right])
                right -= 1

            # bottom
            for a in range(right, left - 1, -1):
                answer.append(matrix[bottom][a])
            bottom -= 1

            # left
            for a in range(bottom, top - 1, -1):
                answer.append(matrix[a][left])
            left += 1

        return answer[:total]

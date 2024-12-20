"""
Link: https://leetcode.com/problems/most-beautiful-item-for-each-query/
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        maxi = [0]

        for _, beauty in items:
            maxi.append(max(maxi[-1], beauty))

        def custom_bisect_right(query):
            left, right = 0, len(items)

            while left < right:
                mid = (left + right) >> 1
                if items[mid][0] <= query:
                    left = mid + 1
                else:
                    right = mid

            return left

        answer = []
        for query in queries:
            index = custom_bisect_right(query)
            answer.append(maxi[index])

        return answer

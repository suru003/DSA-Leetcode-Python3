"""
Link: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
Time Complexity: O(m log(max(quantities)))
Space Complexity: O(1)
"""
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(max_product):
            count = 0

            for quantity in quantities:
                div, mod = divmod(quantity, max_product)
                count += div + (mod > 0)

            return count <= n

        left, right = 1, sum(quantities)

        while left < right:
            mid = (left + right) >> 1
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1

        return right

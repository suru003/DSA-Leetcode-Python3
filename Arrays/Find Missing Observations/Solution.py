"""
Link: https://leetcode.com/problems/find-missing-observations/
Time Complexity: O(n + m)
Space Complexity: O(n)
"""
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        denom = n + m
        total = sum(rolls)

        expected = denom * mean
        missing_total = expected - total

        if missing_total > 6 * n or missing_total < 1:
            return []

        missing_div, missing_mod = divmod(missing_total, n)
        if missing_div == 0:
            return []

        to_return = [missing_div] * n
        for index in range(missing_mod):
            to_return[index] += 1

        return to_return

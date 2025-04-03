"""
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
n = len(prices)
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer, n = 0, len(prices)
        # for second transaction
        profits = [0] * (n + 1)
        max_from_end = 0
        for ind in range(n - 1, -1, -1):
            profits[ind] = max(profits[ind + 1], max_from_end - prices[ind])
            max_from_end = max(max_from_end, prices[ind])

        # for first transaction
        min_from_start = inf
        for ind, val in enumerate(prices):
            first_profit = max(0, val - min_from_start)
            next_profit = profits[ind + 1]
            answer = max(answer, first_profit + next_profit)
            min_from_start = min(min_from_start, val)

        return answer

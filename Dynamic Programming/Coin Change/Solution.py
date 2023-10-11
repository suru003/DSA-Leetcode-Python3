'''
Link: https://leetcode.com/problems/coin-change/
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        for amt in range(amount + 1):
            for coin in coins:
                dp[coin] = 1
                if coin <= amt:
                    dp[amt] = min(dp.get(amt, float("inf")), dp.get(amt - coin, float("inf")) + 1)

        return -1 if dp.get(amount, float("inf")) == float("inf") else dp[amount]

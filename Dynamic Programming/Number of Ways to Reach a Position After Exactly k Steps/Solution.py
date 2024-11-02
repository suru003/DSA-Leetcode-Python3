"""
Link: https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
Time Complexity: O(nk)
Space Complexity: O(nk)
"""

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {}

        def recurse(current, remaining):
            if (current, remaining) in dp:
                return dp[(current, remaining)]

            if not remaining:
                return 1 if current == endPos else 0

            total = 0
            # left
            total += recurse(current - 1, remaining - 1)
            # right
            total += recurse(current + 1, remaining - 1)

            dp[(current, remaining)] = total
            return total

        return recurse(startPos, k) % MOD

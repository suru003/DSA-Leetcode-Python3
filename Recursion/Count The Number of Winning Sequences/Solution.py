"""
Link: https://leetcode.com/problems/count-the-number-of-winning-sequences/
Time Complexity: O(3^n)
Space Complexity: O(3^n)
"""

class Solution:
    def countWinningSequences(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = {}

        def getScore(bob, alice):
            if bob == alice:
                return 0

            if (bob == 'F' and alice == 'E') \
                    or (bob == 'W' and alice == 'F') \
                    or (bob == 'E' and alice == 'W'):
                return 1

            return -1

        def recurse(index, score, last):
            if score + n - index < 1:
                return 0

            if index == n:
                return 1

            if (index, score, last) in dp:
                return dp[(index, score, last)]

            total = 0

            for current in 'FEW':
                if current != last:
                    # Bob summons, Alice summons
                    dx = getScore(current, s[index])

                    total += recurse(index + 1, score + dx, current)

            total %= MOD
            dp[(index, score, last)] = total
            return total

        answer = recurse(0, 0, '')
        return answer

'''
Link: https://leetcode.com/problems/happy-number/
Time Complexity: ??
Space Complexity: ??
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            cur = 0
            while n:
                n, mod = divmod(n, 10)
                cur += mod ** 2
            n = cur

        return True

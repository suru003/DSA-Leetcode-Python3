'''
Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
Time Complexity: O(len(n))
Space Complexity: O(1)
'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        addn, muln = 0, 1

        while n:
            n, mod = divmod(n, 10)
            addn += mod
            muln *= mod

        return muln - addn
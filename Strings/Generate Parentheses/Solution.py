'''
Link: https://leetcode.com/problems/generate-parentheses/
Time Complexity: O(2^n)
Space Complexity: O(1)
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def recurse(rem, left, cur):
            if rem == 0 and left == 0:
                ans.append(cur)
            else:
                if rem:
                    recurse(rem - 1, left + 1, cur + "(")
                if left:
                    recurse(rem, left - 1, cur + ")")

        recurse(n, 0, "")
        return ans

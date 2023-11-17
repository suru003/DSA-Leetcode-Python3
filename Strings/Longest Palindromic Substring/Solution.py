'''
Link: https://leetcode.com/problems/longest-palindromic-substring/
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def longestPalindrome(self, s):
        res = ""

        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1;
                r += 1
            return s[l + 1: r]

        for i in range(len(s)):
            tmp = helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp

        return res

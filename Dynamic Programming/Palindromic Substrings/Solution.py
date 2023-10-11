'''
Link: https://leetcode.com/problems/palindromic-substrings/
Time Complexity: O(n^2)
Space Complexity: O(1)
'''

class Solution:
    def countSubstrings(self, s: str) -> int:

        def getOddPals(index):
            cnt = 1
            for i in range(1, min(index + 1, len(s) - index)):
                if s[index - i] != s[index + i]:
                    break
                cnt += 1

            return cnt

        def getEvenPals(index):
            nex = index + 1
            if nex >= len(s) or s[index] != s[nex]:
                return 0

            cnt = 1
            for i in range(1, min(index + 1, len(s) - nex)):
                if s[index - i] != s[nex + i]:
                    break
                cnt += 1

            return cnt

        total = 0
        for i in range(len(s)):
            total += getOddPals(i)
            total += getEvenPals(i)

        return total

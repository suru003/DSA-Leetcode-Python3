'''
Link: https://leetcode.com/problems/number-of-matching-subsequences/
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''
from typing import List
from bisect import bisect_right
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count, indices = 0, defaultdict(list)

        for i in range(len(s)):
            indices[s[i]].append(i)

        def isValidSubsequence(word):
            currIndex = -1
            for char in word:
                position = bisect_right(indices[char], currIndex)

                if len(indices[char]) == position:
                    return False

                currIndex = indices[char][position]

            return True

        for word in words:
            if isValidSubsequence(word):
                count += 1

        return count

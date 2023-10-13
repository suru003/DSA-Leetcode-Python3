'''
Link: https://leetcode.com/problems/number-of-matching-subsequences/
Time Complexity: O(n*len(s))
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(words)
        curPointers = [0] * n

        for char in s:
            for index in range(n):
                if len(words[index]) > curPointers[index] and words[index][curPointers[index]] == char:
                    curPointers[index] += 1

        count = 0
        for index in range(n):
            if len(words[index]) == curPointers[index]:
                count += 1

        return count

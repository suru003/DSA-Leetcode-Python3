'''
Link: https://leetcode.com/problems/word-ladder/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dq = deque()
        dq.append((beginWord, 1))

        wordSet = set(wordList)

        while dq:
            current, hops = dq.popleft()
            if current == endWord:
                return hops

            for index in range(len(current)):
                for offset in range(26):
                    nextWord = current[:index] + chr(ord('a') + offset) + current[index + 1:]
                    if nextWord in wordSet:
                        dq.append((nextWord, hops + 1))
                        wordSet.remove(nextWord)

        return 0

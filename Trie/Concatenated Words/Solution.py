"""
Link: https://leetcode.com/problems/concatenated-words/
Time Complexity: O(N*L^2)
Space Complexity: O(N*L)
"""
from functools import cache
from typing import List


class TrieNode:
    def __init__(self, val: str, is_end: bool = False):
        self.val = val
        self.children = {}
        self.is_end = is_end


class Solution:
    def __init__(self):
        self.trie = TrieNode('-')

    def add_word(self, word: str):
        ptr = self.trie

        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TrieNode(char)

            ptr = ptr.children[char]

        ptr.is_end = True

    # cache should not be required to run but because of Leetcode's runtime it's required
    @cache
    def dfs(self, root: TrieNode, string: str, index: int, count: int):
        if index == len(string):
            return count > 1

        ptr = root
        for i in range(index, len(string)):
            if string[i] not in ptr.children:
                return False

            ptr = ptr.children[string[i]]
            if ptr.is_end:
                if self.dfs(root, string, i + 1, count + 1):
                    return True

        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        for word in words:
            self.add_word(word)

        answer = []
        for word in words:
            if self.dfs(self.trie, word, 0, 0):
                answer.append(word)

        return answer

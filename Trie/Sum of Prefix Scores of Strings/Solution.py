"""
Link: https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
Time Complexity: O(N*M)
Space Complexity: O(N*M)
"""
from typing import List


class Node:
    def __init__(self, val, score):
        self.val = val
        self.score = score
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node('-', 0)

    def add_word(self, word):
        ptr = self.root

        for char in word:
            if char not in ptr.children:
                ptr.children[char] = Node(char, 0)

            ptr = ptr.children[char]
            ptr.score += 1

    def get_score(self, word):
        ptr = self.root
        score = 0

        for char in word:
            if char not in ptr.children:
                break

            ptr = ptr.children[char]
            score += ptr.score

        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add_word(word)

        return [trie.get_score(word) for word in words]

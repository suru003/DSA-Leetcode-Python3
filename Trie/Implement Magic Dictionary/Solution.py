"""
Link: https://leetcode.com/problems/implement-magic-dictionary/
Time Complexity: O(N*L^2)
Space Complexity: O(L)
"""
from typing import List


class TrieNode:
    def __init__(self, val: str, is_end: bool = False):
        self.val = val
        self.children = {}
        self.is_end = is_end


class MagicDictionary:
    def __init__(self):
        self.trie = TrieNode('-')

    def add_word(self, word: str):
        ptr = self.trie

        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TrieNode(char)

            ptr = ptr.children[char]

        ptr.is_end = True

    def dfs(self, ptr, searchWord, index, changes):
        if index == len(searchWord) - 1:
            valid = False
            for key in ptr.children.keys():
                if ptr.children[key].is_end:
                    if key != searchWord[index]:
                        valid = valid or changes == 0
                    else:
                        valid = valid or changes == 1

            return valid

        if searchWord[index] in ptr.children:
            if self.dfs(ptr.children[searchWord[index]], searchWord, index + 1, changes):
                return True

        for key in ptr.children.keys():
            if key != searchWord[index] and not changes:
                if self.dfs(ptr.children[key], searchWord, index + 1, changes + 1):
                    return True

        return False

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.add_word(word)

    def search(self, searchWord: str) -> bool:
        return self.dfs(self.trie, searchWord, 0, 0)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
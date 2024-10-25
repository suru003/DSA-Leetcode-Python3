"""
Link: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
Time Complexity: O(N * M)
Space Complexity: O(N * M)
"""
from typing import List

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.is_end = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode('/')

    def add_folder(self, path):
        folders = path.split('/')
        ptr = self.root

        for folder in folders:
            if folder not in ptr.children:
                ptr.children[folder] = TrieNode(folder)

            ptr = ptr.children[folder]

        ptr.is_end = True

    def get_parent_paths(self):
        paths = []

        def dfs(ptr, folders):
            if ptr.is_end:
                paths.append('/'.join(folders))
            else:
                for child_folder in ptr.children:
                    folders.append(child_folder)
                    dfs(ptr.children[child_folder], folders)
                    folders.pop()

        dfs(self.root, [])
        return paths


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        for path in folder:
            trie.add_folder(path)

        return trie.get_parent_paths()

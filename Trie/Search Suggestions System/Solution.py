"""
Link: https://leetcode.com/problems/search-suggestions-system/
Time Complexity: O(n * logn)
Space Complexity: O(n * k * m)
"""
from collections import defaultdict
from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = defaultdict(TrieNode)
                self.suggestion = []

            def add_sugestion(self, product):
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)

        products = sorted(products)
        root = TrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_sugestion(p)

        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append(node.suggestion)

        return result
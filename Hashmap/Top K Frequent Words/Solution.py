'''
Link: https://leetcode.com/problems/top-k-frequent-words/
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = Counter(words)
        items = sorted([(v, k) for k, v in dic.items()], key=lambda x: [-x[0], x[1]])

        return [string for _, string in items[:k]]

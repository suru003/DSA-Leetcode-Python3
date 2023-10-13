'''
Link: https://leetcode.com/problems/number-of-matching-subsequences/
Time Complexity: O(n*len(s))
Space Complexity: O(n)
'''
from typing import List
from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2: return []

        sortedArray = sorted(changed, reverse=True)
        counts = Counter(changed)
        answer = []

        for num in sortedArray:
            div, mod = divmod(num, 2)
            if counts[num] and (mod or counts.get(div, 0) == 0):
                return []

            if counts[num]:
                counts[num] -= 1
                counts[div] -= 1
                answer.append(div)

        return answer

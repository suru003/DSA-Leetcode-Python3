"""
Link: https://leetcode.com/problems/snapshot-array/
n, m = len(spells), len(potions)
Time Complexity: O(nlogm + mlogm)
Space Complexity: O(n)
"""
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        answer = []

        def get_potions(spell):
            n = len(potions)
            l, r = 0, n - 1
            min_ind = n

            while l <= r:
                mid = (l + r) >> 1
                potion_strength = potions[mid] * spell
                if potion_strength < success:
                    l = mid + 1
                else:
                    r = mid - 1
                    min_ind = mid

            return n - min_ind

        for spell in spells:
            answer.append(get_potions(spell))

        return answer

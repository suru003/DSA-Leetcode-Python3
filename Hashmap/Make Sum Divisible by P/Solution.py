'''
Link: https://leetcode.com/problems/make-sum-divisible-by-p/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List
from collections import defaultdict

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mods_indices = defaultdict(list)
        cur_mod = 0
        length = len(nums)
        min_length = length

        for index, num in enumerate(nums):
            cur_mod = (cur_mod + num) % p
            mods_indices[cur_mod].append(index)

            if not cur_mod:
                min_length = min(min_length, length - index - 1)

        if not cur_mod:
            return cur_mod

        cur_mod = 0
        for index in range(len(nums) - 1, 0, -1):
            num = nums[index]
            cur_mod = (cur_mod + num) % p

            if not cur_mod:
                min_length = min(min_length, index)

            target_mod = p - cur_mod
            while mods_indices[target_mod] and mods_indices[target_mod][-1] >= index - 1:
                mods_indices[target_mod].pop()

            if mods_indices[target_mod]:
                min_length = min(min_length, index - mods_indices[target_mod][-1] - 1)

        return -1 if min_length == len(nums) else min_length

"""
Link: https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
from collections import defaultdict


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        setbits = defaultdict(int)
        n = len(nums)
        cur_val = 0
        answer = n + 1
        i, j = 0, 0

        if k == 0:
            return 1

        def getValue(setbits):
            cur_val = 0

            for key, val in setbits.items():
                if val:
                    cur_val += (2 ** key)

            return cur_val

        while j < n:
            # move right pointer
            while j < n and cur_val < k:
                cur_val |= nums[j]

                binary = str(bin(nums[j]))[2:][::-1]
                for index, val in enumerate(binary):
                    setbits[index] += (1 if val == '1' else 0)

                j += 1

            # move left pointer
            while i < n and cur_val >= k:
                answer = min(answer, j - i)

                binary = str(bin(nums[i]))[2:][::-1]
                for index, val in enumerate(binary):
                    setbits[index] -= (1 if val == '1' else 0)

                cur_val = getValue(setbits)
                i += 1

        return -1 if answer == n + 1 else answer

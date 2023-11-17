'''
Link: https://leetcode.com/problems/subarray-sum-equals-k/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        current, cnt = 0, 0

        for num in nums:
            current += num
            rem = current - k
            cnt += seen[rem]
            seen[current] += 1

        return cnt

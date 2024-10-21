"""
Link: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/
Time Complexity: O(n * klogk)
Space Complexity: O(k)
"""
from typing import List
from collections import defaultdict

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        counts = defaultdict(int)
        answer = []

        for i in range(len(nums)):
            if i >= k:
                counts[nums[i - k]] -= 1

            counts[nums[i]] += 1
            if i >= k - 1:
                most_freq = sorted(counts.items(), key=lambda x: [-x[1], -x[0]])
                temp_sum = 0
                for key, val in most_freq[:x]:
                    temp_sum += key * val

                answer.append(temp_sum)

        return answer

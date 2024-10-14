'''
Link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        nums_inds = []
        ind_length = len(nums)
        for ind in range(ind_length):
            for val in nums[ind]:
                nums_inds.append([val, ind])

        nums_inds.sort()
        nums_inds_len = len(nums_inds)
        i, j = 0, 0
        counts = [0] * nums_inds_len
        non_zeroes = 0

        min_range = nums_inds[-1][0] - nums_inds[0][0]
        answer_range = [nums_inds[0][0], nums_inds[-1][0]]

        def is_valid():
            return non_zeroes == ind_length

        while j < nums_inds_len:
            while j < nums_inds_len and not is_valid():
                val, ind = nums_inds[j]

                if counts[ind] == 0:
                    non_zeroes += 1

                counts[ind] += 1
                j += 1

            while i < j and is_valid():
                a, ind_i = nums_inds[i]
                # Since it would have been incremented in the prev loop
                b, ind_j = nums_inds[j - 1]

                temp_range = b - a
                if temp_range < min_range:
                    min_range = temp_range
                    answer_range = [a, b]

                counts[ind_i] -= 1
                if counts[ind_i] == 0:
                    non_zeroes -= 1

                i += 1

        return answer_range

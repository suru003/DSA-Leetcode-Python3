"""
Link: https://leetcode.com/problems/xor-queries-of-a-subarray/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        BITS = 40
        ones = [[0] * BITS]

        for val in arr:
            temp = ones[-1][:]
            cur = str(bin(val))[::-1]

            for index, bit in enumerate(cur):
                if bit == 'b': break

                if bit == '1':
                    temp[index] += 1

            ones.append(temp)

        answer = []
        for a, b in queries:
            left = ones[a]
            right = ones[b + 1]
            val = 0

            for index in range(BITS):
                if (right[index] - left[index]) % 2:
                    val = val + 2 ** index

            answer.append(val)

        return answer

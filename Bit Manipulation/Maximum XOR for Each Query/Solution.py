"""
Link: https://leetcode.com/problems/maximum-xor-for-each-query/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = []
        current = None

        for val in nums:
            if current:
                current ^= val
            else:
                current = val

            binary = str(bin(current))[2:]
            binary = ('0' * (maximumBit - len(binary))) + binary

            current_answer = 0
            for ind in range(maximumBit):
                if binary[ind] == '0':
                    current_answer += 2 ** (maximumBit - ind - 1)

            answer.append(current_answer)

        return answer[::-1]

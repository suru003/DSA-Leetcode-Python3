"""
Link: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        n -= 1
        bits = ['0']

        for i in range(1, n + 1):
            prev_length = len(bits)
            bits.append('1')

            for cur_index in range(prev_length - 1, -1, -1):
                bits.append('0' if bits[cur_index] == '1' else '1')

        return bits[k - 1]

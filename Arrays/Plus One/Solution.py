'''
Link: https://leetcode.com/problems/plus-one/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        for digit in digits:
            total = total * 10 + digit

        return [int(digit) for digit in str(total + 1)]

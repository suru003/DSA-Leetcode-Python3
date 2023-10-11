'''
Link: https://leetcode.com/problems/daily-temperatures/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, n = [], len(temperatures)
        ans = [0] * n

        for index in range(n):
            while stack and temperatures[stack[-1]] < temperatures[index]:
                updateAt = stack.pop()
                ans[updateAt] = index - updateAt

            stack.append(index)

        return ans

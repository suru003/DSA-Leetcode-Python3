'''
Link: https://leetcode.com/problems/remove-k-digits/
Time Complexity: O(len(nums))
Space Complexity: O(n)
'''

class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        if k == len(nums):
            return '0'

        stack = []
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and k:
                stack.pop()
                k -= 1

            stack.append(num)

        leadingZeroes = 0
        for leadingZeroes in range(len(stack)):
            if stack[leadingZeroes] != '0':
                break

        answer = ''.join(stack[leadingZeroes: len(stack) - k])
        return answer if answer else "0"

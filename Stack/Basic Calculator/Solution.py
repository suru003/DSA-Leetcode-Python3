'''
Link: https://leetcode.com/problems/basic-calculator/
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def calculate(self, s: str) -> int:
        s = "(" + s.replace(" ", "") + ")"
        cur, level, n = 0, 0, len(s)
        stack = []

        while cur < n:
            if s[cur] == "(":
                level += 1

            elif s[cur] == ")":
                level -= 1
                stack[-1][1] = level

            elif s[cur] in "+-":
                stack.append([s[cur], level])

            else:
                # numbers (can be multi digits)
                num = ""
                while s[cur] not in "(+-)":
                    num += s[cur]
                    cur += 1

                num = int(num, 10)
                stack.append([num, level])
                cur -= 1

            # Perform operation
            while len(stack) > 2 and stack[-2][1] == stack[-1][1] == stack[-3][1]:
                right, sym, left = stack.pop(), stack.pop(), stack.pop()
                if sym[0] == "+":
                    stack.append([left[0] + right[0], left[1]])
                else:
                    stack.append([left[0] - right[0], left[1]])

            # Negative number
            while len(stack) > 1 and stack[-2][1] == stack[-1][1] and stack[-2][0] == "-":
                right, sym = stack.pop(), stack.pop()
                stack.append([-right[0], right[1]])

            cur += 1
        return stack[-1][0]

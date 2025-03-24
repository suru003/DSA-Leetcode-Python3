"""
Link: https://leetcode.com/problems/shortest-common-supersequence
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1 = '#' + str1
        str2 = '*' + str2

        len1, len2 = len(str1), len(str2)

        dp = [[0] * len2 for _ in range(len1)]

        for i in range(len1):
            for j in range(len2):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                if str1[i] == str2[j]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i - 1][j - 1])

        common_stack = []
        row, col = len1 - 1, len2 - 1
        while row >= 0 and col >= 0 and dp[row][col]:
            prev = max(dp[row][col - 1], dp[row - 1][col])
            curr = dp[row][col]
            if prev != curr:
                common_stack.append(str1[row])
                row -= 1
                col -= 1
            elif dp[row][col - 1] > dp[row - 1][col]:
                col -= 1
            else:
                row -= 1

        ptr1, ptr2 = 1, 1
        answer = []
        while common_stack \
                and ptr1 < len1 and ptr2 < len2:

            while common_stack \
                    and ptr1 < len1 and common_stack[-1] != str1[ptr1]:
                answer.append(str1[ptr1])
                ptr1 += 1

            while common_stack \
                    and ptr2 < len2 and common_stack[-1] != str2[ptr2]:
                answer.append(str2[ptr2])
                ptr2 += 1

            answer.append(common_stack.pop())
            ptr1 += 1
            ptr2 += 1

        return ''.join(answer) + str1[ptr1:] + str2[ptr2:]

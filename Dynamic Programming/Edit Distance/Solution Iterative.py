"""
Link: https://leetcode.com/problems/edit-distance/
Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""


class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    """
                    Insert: table[i][j - 1] + 1 (insert the character from word2 into word1).
                    Delete: table[i - 1][j] + 1 (delete the character from word1).
                    Substitute: table[i - 1][j - 1] + 1 (replace the character from word1 with the character from word2).
                    """
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])

        return table[-1][-1]

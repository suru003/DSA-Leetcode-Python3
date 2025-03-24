class Solution {
    public String shortestCommonSupersequence(String str1, String str2) {
        str1 = "#" + str1;
        str2 = "*" + str2;

        int len1 = str1.length();
        int len2 = str2.length();

        int[][] dp = new int[len1][len2];

        // Fill the dp table
        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                dp[i][j] = Math.max(
                    j > 0 ? dp[i][j-1] : 0,
                    i > 0 ? dp[i-1][j] : 0
                );
                if (str1.charAt(i) == str2.charAt(j)) {
                    dp[i][j] = Math.max(
                        dp[i][j],
                        1 + (i > 0 && j > 0 ? dp[i-1][j-1] : 0)
                    );
                }
            }
        }

        // Build common sequence
        Stack<Character> commonStack = new Stack<>();
        int row = len1 - 1;
        int col = len2 - 1;

        while (row >= 0 && col >= 0 && dp[row][col] > 0) {
            int prev = Math.max(
                col > 0 ? dp[row][col-1] : 0,
                row > 0 ? dp[row-1][col] : 0
            );
            int curr = dp[row][col];

            if (prev != curr) {
                commonStack.push(str1.charAt(row));
                row--;
                col--;
            } else if (col > 0 && dp[row][col-1] > (row > 0 ? dp[row-1][col] : 0)) {
                col--;
            } else {
                row--;
            }
        }

        // Build final answer
        StringBuilder answer = new StringBuilder();
        int ptr1 = 1;
        int ptr2 = 1;

        while (!commonStack.empty() && ptr1 < len1 && ptr2 < len2) {
            while (!commonStack.empty() && ptr1 < len1 &&
                   commonStack.peek() != str1.charAt(ptr1)) {
                answer.append(str1.charAt(ptr1));
                ptr1++;
            }

            while (!commonStack.empty() && ptr2 < len2 &&
                   commonStack.peek() != str2.charAt(ptr2)) {
                answer.append(str2.charAt(ptr2));
                ptr2++;
            }

            answer.append(commonStack.pop());
            ptr1++;
            ptr2++;
        }

        // Append remaining characters
        while (ptr1 < len1) {
            answer.append(str1.charAt(ptr1));
            ptr1++;
        }

        while (ptr2 < len2) {
            answer.append(str2.charAt(ptr2));
            ptr2++;
        }

        return answer.toString();
    }
}

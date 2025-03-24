func shortestCommonSupersequence(str1 string, str2 string) string {
    // Add dummy characters at start
    str1 = "#" + str1
    str2 = "*" + str2

    len1, len2 := len(str1), len(str2)

    // Create DP table
    dp := make([][]int, len1)
    for i := range dp {
        dp[i] = make([]int, len2)
    }

    // Fill DP table
    for i := 0; i < len1; i++ {
        for j := 0; j < len2; j++ {
            // Get max of left and top
            if j > 0 {
                dp[i][j] = dp[i][j-1]
            }
            if i > 0 && dp[i-1][j] > dp[i][j] {
                dp[i][j] = dp[i-1][j]
            }
            // If characters match, consider diagonal + 1
            if str1[i] == str2[j] {
                curr := 1
                if i > 0 && j > 0 {
                    curr += dp[i-1][j-1]
                }
                if curr > dp[i][j] {
                    dp[i][j] = curr
                }
            }
        }
    }

    // Build common sequence stack
    var commonStack []byte
    row, col := len1-1, len2-1

    for row >= 0 && col >= 0 && dp[row][col] > 0 {
        prev := 0
        if col > 0 {
            prev = dp[row][col-1]
        }
        if row > 0 && dp[row-1][col] > prev {
            prev = dp[row-1][col]
        }

        curr := dp[row][col]
        if prev != curr {
            commonStack = append(commonStack, str1[row])
            row--
            col--
        } else if col > 0 && dp[row][col-1] > func() int {
            if row > 0 {
                return dp[row-1][col]
            }
            return 0
        }() {
            col--
        } else {
            row--
        }
    }

    // Build final answer
    var result []byte
    ptr1, ptr2 := 1, 1

    for len(commonStack) > 0 && ptr1 < len1 && ptr2 < len2 {
        // Add characters from str1 until common character
        for len(commonStack) > 0 && ptr1 < len1 &&
            commonStack[len(commonStack)-1] != str1[ptr1] {
            result = append(result, str1[ptr1])
            ptr1++
        }

        // Add characters from str2 until common character
        for len(commonStack) > 0 && ptr2 < len2 &&
            commonStack[len(commonStack)-1] != str2[ptr2] {
            result = append(result, str2[ptr2])
            ptr2++
        }

        // Add common character
        if len(commonStack) > 0 {
            result = append(result, commonStack[len(commonStack)-1])
            commonStack = commonStack[:len(commonStack)-1]
            ptr1++
            ptr2++
        }
    }

    // Add remaining characters
    for ptr1 < len1 {
        result = append(result, str1[ptr1])
        ptr1++
    }

    for ptr2 < len2 {
        result = append(result, str2[ptr2])
        ptr2++
    }

    return string(result)
}

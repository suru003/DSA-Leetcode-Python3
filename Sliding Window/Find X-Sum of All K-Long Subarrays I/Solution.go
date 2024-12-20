package main

import (
    "math"
    "strconv"
)

func minimumSubarrayLength(nums []int, k int) int {
    setBits := make(map[int]int)
    n := len(nums)
    curVal := 0
    answer := n + 1
    i, j := 0, 0

    if k == 0 {
        return 1
    }

    // Helper function to calculate the current value based on set bits
    getValue := func(setBits map[int]int) int {
        curVal := 0
        for key, val := range setBits {
            if val > 0 {
                curVal += int(math.Pow(2, float64(key)))
            }
        }
        return curVal
    }

    for j < n {
        // Move right pointer
        for j < n && curVal < k {
            curVal |= nums[j]
            binary := strconv.FormatInt(int64(nums[j]), 2)

            // Reverse binary and update setBits map
            for index, val := range reverse(binary) {
                if val == '1' {
                    setBits[index]++
                }
            }
            j++
        }

        // Move left pointer
        for i < n && curVal >= k {
            if j-i < answer {
                answer = j - i
            }

            binary := strconv.FormatInt(int64(nums[i]), 2)

            // Reverse binary and update setBits map
            for index, val := range reverse(binary) {
                if val == '1' {
                    setBits[index]--
                }
            }
            curVal = getValue(setBits)
            i++
        }
    }

    if answer == n+1 {
        return -1
    }
    return answer
}

// Helper function to reverse a string
func reverse(s string) string {
    r := []rune(s)
    for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}

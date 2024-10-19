package main

import (
	"fmt"
)

var dp map[string]int
var maxi int

// Standalone countMaxOrSubsets function
func countMaxOrSubsets(nums []int) int {
	// Initialize dp map and maxi
	dp = make(map[string]int)
	maxi = 0

	// Calculate maximum OR value for nums array
	for _, val := range nums {
		maxi |= val
	}

	// Call recursive function starting from index 0 and current OR value 0
	return recurse(0, 0, nums)
}

// Recursive function for subset OR calculation
func recurse(index, current int, nums []int) int {
	key := fmt.Sprintf("%d,%d", index, current) // Generate unique key for memoization
	if val, ok := dp[key]; ok {
		return val
	}

	if index == len(nums) {
		if current == maxi {
			return 1
		}
		return 0
	}

	// Option 1: Ignore current number
	op1 := recurse(index+1, current, nums)

	// Option 2: Use current number
	op2 := recurse(index+1, current|nums[index], nums)

	dp[key] = op1 + op2
	return op1 + op2
}

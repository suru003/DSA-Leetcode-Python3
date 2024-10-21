package main

import (
	"fmt"
	"strconv"
)

const MOD = 1000000007

func countWinningSequences(s string) int {
	n := len(s)
	dp := make(map[string]int)

	// Function to determine the score based on Bob's and Alice's choices.
	getScore := func(bob, alice byte) int {
		if bob == alice {
			return 0
		}
		if (bob == 'F' && alice == 'E') || (bob == 'W' && alice == 'F') || (bob == 'E' && alice == 'W') {
			return 1
		}
		return -1
	}

	// Recursive function with memoization.
	var recurse func(index int, score int, last byte) int
	recurse = func(index, score int, last byte) int {
		if score+n-index < 1 {
			return 0
		}
		if index == n {
			return 1
		}

		// Memoization key (combination of index, score, and last)
		key := strconv.Itoa(index) + "," + strconv.Itoa(score) + "," + string(last)
		if val, exists := dp[key]; exists {
			return val
		}

		total := 0

		// Iterate over the three possible choices 'F', 'E', 'W'
		for _, current := range []byte{'F', 'E', 'W'} {
			if current != last {
				dx := getScore(current, s[index])
				total = (total + recurse(index+1, score+dx, current)) % MOD
			}
		}

		dp[key] = total
		return total
	}

	return recurse(0, 0, ' ')
}

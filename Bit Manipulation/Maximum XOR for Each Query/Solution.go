package main

import (
	"fmt"
)

func getMaximumXor(nums []int, maximumBit int) []int {
	answer := []int{}
	var current int

	for _, val := range nums {
		if current != 0 {
			current ^= val
		} else {
			current = val
		}

		binary := fmt.Sprintf("%0*b", maximumBit, current)

		currentAnswer := 0
		for ind := 0; ind < maximumBit; ind++ {
			if binary[ind] == '0' {
				currentAnswer += 1 << (maximumBit - ind - 1)
			}
		}

		answer = append(answer, currentAnswer)
	}

	// Reverse the answer slice
	for i, j := 0, len(answer)-1; i < j; i, j = i+1, j-1 {
		answer[i], answer[j] = answer[j], answer[i]
	}

	return answer
}

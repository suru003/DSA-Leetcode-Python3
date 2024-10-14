package main

import (
	"fmt"
	"sort"
)

func smallestRange(nums [][]int) []int {
	numsInds := [][]int{}
	indLength := len(nums)

	// Flatten the nums array with indices
	for ind := 0; ind < indLength; ind++ {
		for _, val := range nums[ind] {
			numsInds = append(numsInds, []int{val, ind})
		}
	}

	// Sort numsInds by the value (first element of each pair)
	sort.Slice(numsInds, func(i, j int) bool {
		return numsInds[i][0] < numsInds[j][0]
	})

	numsIndsLen := len(numsInds)
	i, j := 0, 0
	counts := make([]int, indLength)
	nonZeroes := 0
	minRange := numsInds[numsIndsLen-1][0] - numsInds[0][0]
	answerRange := []int{numsInds[0][0], numsInds[numsIndsLen-1][0]}

	// Helper function to check if all lists are represented in the current window
	isValid := func() bool {
		return nonZeroes == indLength
	}

	for j < numsIndsLen {
		for j < numsIndsLen && !isValid() {
			_, ind := numsInds[j][0], numsInds[j][1]
			if counts[ind] == 0 {
				nonZeroes++
			}
			counts[ind]++
			j++
		}

		for i < j && isValid() {
			a, ind_i := numsInds[i][0], numsInds[i][1]
			b := numsInds[j-1][0]

			tempRange := b - a
			if tempRange < minRange {
				minRange = tempRange
				answerRange = []int{a, b}
			}

			counts[ind_i]--
			if counts[ind_i] == 0 {
				nonZeroes--
			}
			i++
		}
	}

	return answerRange
}

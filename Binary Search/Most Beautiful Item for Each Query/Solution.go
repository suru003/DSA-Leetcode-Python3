package main

import (
	"sort"
)

func maximumBeauty(items [][]int, queries []int) []int {
	// Sort items by price
	sort.Slice(items, func(i, j int) bool {
		return items[i][0] < items[j][0]
	})

	// Generate the max beauty array
	maxi := make([]int, len(items)+1)
	for i, item := range items {
		maxi[i+1] = max(maxi[i], item[1])
	}

	// Custom binary search function
	customBisectRight := func(query int) int {
		left, right := 0, len(items)
		for left < right {
			mid := (left + right) >> 1
			if items[mid][0] <= query {
				left = mid + 1
			} else {
				right = mid
			}
		}
		return left
	}

	// Process each query
	answer := make([]int, len(queries))
	for i, query := range queries {
		index := customBisectRight(query)
		answer[i] = maxi[index]
	}

	return answer
}

// Utility function to find the maximum of two integers
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

package main

import (
	"fmt"
	"sort"
)

func minGroups(intervals [][]int) int {
	dic := make(map[int]int)

	// Populate the dictionary with start and end points
	for _, interval := range intervals {
		start, end := interval[0], interval[1]
		dic[start]++
		dic[end+1]--
	}

	// Extract and sort keys
	keys := make([]int, 0, len(dic))
	for key := range dic {
		keys = append(keys, key)
	}
	sort.Ints(keys)

	// Calculate max groups required
	cur, maxi := 0, 0
	for _, key := range keys {
		cur += dic[key]
		if cur > maxi {
			maxi = cur
		}
	}

	return maxi
}

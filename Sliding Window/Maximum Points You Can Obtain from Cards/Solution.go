package main

import (
	"sort"
)

func findXSum(nums []int, k int, x int) []int {
	counts := make(map[int]int)
	var answer []int

	for i := 0; i < len(nums); i++ {
		// Remove the element that is out of the sliding window
		if i >= k {
			counts[nums[i-k]]--
			if counts[nums[i-k]] == 0 {
				delete(counts, nums[i-k])
			}
		}

		// Add current element to the map
		counts[nums[i]]++

		// Once we have a full window, calculate the x most frequent sum
		if i >= k-1 {
			mostFreq := make([][2]int, 0, len(counts))
			for key, val := range counts {
				mostFreq = append(mostFreq, [2]int{key, val})
			}

			// Sort by frequency and value
			sort.Slice(mostFreq, func(a, b int) bool {
				if mostFreq[a][1] == mostFreq[b][1] {
					return mostFreq[a][0] > mostFreq[b][0] // Sort by value in descending
				}
				return mostFreq[a][1] > mostFreq[b][1] // Sort by frequency in descending
			})

			tempSum := 0
			for j := 0; j < x && j < len(mostFreq); j++ {
				tempSum += mostFreq[j][0] * mostFreq[j][1]
			}

			answer = append(answer, tempSum)
		}
	}

	return answer
}

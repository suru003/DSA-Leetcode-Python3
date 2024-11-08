package main

import (
	"strconv"
)

func canSortArray(nums []int) bool {
	i, n := 0, len(nums)
	prevMax := 0

	getOnes := func(num int) int {
		binaryStr := strconv.FormatInt(int64(num), 2)
		count := 0
		for _, char := range binaryStr {
			if char == '1' {
				count++
			}
		}
		return count
	}

	for i < n {
		windowOnes := getOnes(nums[i])
		mini, maxi := nums[i], nums[i]

		j := i + 1
		for j < n && getOnes(nums[j]) == windowOnes {
			if nums[j] < mini {
				mini = nums[j]
			}
			if nums[j] > maxi {
				maxi = nums[j]
			}
			j++
		}

		if mini < prevMax {
			return false
		}

		prevMax = maxi
		i = j
	}

	return true
}

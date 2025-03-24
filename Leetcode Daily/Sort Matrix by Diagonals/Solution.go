// https://leetcode.com/problems/sort-matrix-by-diagonals/

package main

import (
	"sort"
)

func sortMatrix(grid [][]int) [][]int {
	m := len(grid)
	n := len(grid[0])

	// Sort diagonals starting from the last row
	for row := m - 1; row >= 0; row-- {
		tempList := []int{}
		x, y := row, 0
		for x < m && y < n {
			tempList = append(tempList, grid[x][y])
			x++
			y++
		}

		sort.Sort(sort.Reverse(sort.IntSlice(tempList))) // Sort in descending order
		index := 0
		x, y = row, 0
		for x < m && y < n {
			grid[x][y] = tempList[index]
			x++
			y++
			index++
		}
	}

	// Sort diagonals starting from the last column
	for col := n - 1; col > 0; col-- {
		tempList := []int{}
		x, y := 0, col
		for x < m && y < n {
			tempList = append(tempList, grid[x][y])
			x++
			y++
		}

		sort.Ints(tempList) // Sort in ascending order
		index := 0
		x, y = 0, col
		for x < m && y < n {
			grid[x][y] = tempList[index]
			x++
			y++
			index++
		}
	}

	return grid
}
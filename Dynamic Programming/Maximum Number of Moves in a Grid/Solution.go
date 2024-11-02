package main

import "fmt"

type Coord struct {
	i, j int
}

func maxMoves(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dp := make(map[Coord]int)
	adj := [][2]int{{-1, 1}, {0, 1}, {1, 1}}
	var recurse func(i, j int) int

	recurse = func(i, j int) int {
		if val, exists := dp[Coord{i, j}]; exists {
			return val
		}

		nextMoves := 0
		for _, direction := range adj {
			newI, newJ := i+direction[0], j+direction[1]
			if newI >= 0 && newI < m && newJ >= 0 && newJ < n && grid[newI][newJ] > grid[i][j] {
				nextMoves = max(nextMoves, 1+recurse(newI, newJ))
			}
		}

		dp[Coord{i, j}] = nextMoves
		return nextMoves
	}

	ans := 0
	for i := 0; i < m; i++ {
		ans = max(ans, recurse(i, 0))
	}

	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

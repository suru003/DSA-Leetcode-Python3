package main

import "fmt"

type DSU struct {
	parents map[int]int
	sizes   map[int]int
}

func NewDSU() *DSU {
	return &DSU{
		parents: make(map[int]int),
		sizes:   make(map[int]int),
	}
}

func (dsu *DSU) AddVal(val int) {
	dsu.parents[val] = val
	dsu.sizes[val] = 1
}

func (dsu *DSU) FindParent(val int) int {
	if dsu.parents[val] == val {
		return val
	}
	dsu.parents[val] = dsu.FindParent(dsu.parents[val])
	return dsu.parents[val]
}

func (dsu *DSU) Union(a, b int) {
	parentA := dsu.FindParent(a)
	parentB := dsu.FindParent(b)

	if parentA != parentB {
		if parentA >= parentB {
			dsu.parents[parentB] = parentA
			dsu.sizes[parentA] += dsu.sizes[parentB]
		} else {
			dsu.parents[parentA] = parentB
			dsu.sizes[parentB] += dsu.sizes[parentA]
		}
	}
}

func (dsu *DSU) MaxSize() int {
	max := 1
	for _, size := range dsu.sizes {
		if size > max {
			max = size
		}
	}
	return max
}

func longestSquareStreak(nums []int) int {
	dsu := NewDSU()
	for _, val := range nums {
		dsu.AddVal(val)
	}

	for _, val := range nums {
		next := val * val
		dsu.FindParent(val)

		if _, exists := dsu.parents[next]; exists {
			dsu.Union(val, next)
		}
	}

	answer := dsu.MaxSize()
	if answer == 1 {
		return -1
	}
	return answer
}


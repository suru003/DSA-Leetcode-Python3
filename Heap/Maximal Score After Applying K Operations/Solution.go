package main

import (
	"container/heap"
	"fmt"
	"math"
)

type MaxHeap []int

// Implementing sort.Interface for heap.Interface
func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // For max-heap (reverse order)
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// Push adds an element to the heap
func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

// Pop removes the top element from the heap
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxKelements(nums []int, k int) int64 {
	h := &MaxHeap{}
	heap.Init(h)

	// Push all the numbers into the heap
	for _, num := range nums {
		heap.Push(h, num)
	}

	answer := 0

	for k > 0 {
		// Pop the maximum element
		num := heap.Pop(h).(int)
		answer += num
		// Perform ceil division by 3 and push back to the heap
		num = int(math.Ceil(float64(num) / 3.0)) // Casting to float64 and back to int
		heap.Push(h, num)
		k--
	}

	return int64(answer)
}

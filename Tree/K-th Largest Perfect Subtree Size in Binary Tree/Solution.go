/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package main

import (
	"fmt"
	"sort"
)

func kthLargestPerfectSubtree(root *TreeNode, k int) int {
	treeSizes := []int{}

	var recurse func(*TreeNode) int
	recurse = func(current *TreeNode) int {
		if current == nil {
			return 0
		}

		left := recurse(current.Left)
		right := recurse(current.Right)

		if left != -1 && left == right {
			treeSizes = append(treeSizes, left+right+1)
			return left + right + 1
		}

		return -1
	}

	// Start recursion
	recurse(root)

	// Sort the slice of tree sizes
	sort.Ints(treeSizes)

	// Check if k is valid
	if k > len(treeSizes) {
		return -1
	}

	// Return the kth largest size
	return treeSizes[len(treeSizes)-k]
}

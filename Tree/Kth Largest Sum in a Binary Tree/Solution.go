package main

import (
	"container/list"
	"sort"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func kthLargestLevelSum(root *TreeNode, k int) int64 {
	dq := list.New()
	dq.PushBack([]*TreeNode{root})
	var sums []int

	for dq.Len() > 0 {
		currentLevel := dq.Remove(dq.Front()).([]*TreeNode)
		var nextLevel []*TreeNode
		curSum := 0

		for _, node := range currentLevel {
			curSum += node.Val
			if node.Left != nil {
				nextLevel = append(nextLevel, node.Left)
			}
			if node.Right != nil {
				nextLevel = append(nextLevel, node.Right)
			}
		}

		sums = append(sums, curSum)
		if len(nextLevel) > 0 {
			dq.PushBack(nextLevel)
		}
	}

	sort.Sort(sort.Reverse(sort.IntSlice(sums)))
	if len(sums) < k {
		return -1
	}
	return int64(sums[k-1])
}

package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func reverseOddLevels(root *TreeNode) *TreeNode {
    type Level struct {
        Nodes []*TreeNode
        Flag  bool
    }

    dq := []Level{{Nodes: []*TreeNode{root}, Flag: true}}

    for len(dq) > 0 {
        level := dq[0]
        dq = dq[1:]

        nextLevel := []*TreeNode{}

        for _, node := range level.Nodes {
            if node.Left != nil {
                nextLevel = append(nextLevel, node.Left)
            }
            if node.Right != nil {
                nextLevel = append(nextLevel, node.Right)
            }
        }

        if level.Flag {
            for i := 0; i < len(nextLevel)/2; i++ {
                left := nextLevel[i]
                right := nextLevel[len(nextLevel)-1-i]
                left.Val, right.Val = right.Val, left.Val
            }
        }

        if len(nextLevel) > 0 {
            dq = append(dq, Level{Nodes: nextLevel, Flag: !level.Flag})
        }
    }

    return root
}

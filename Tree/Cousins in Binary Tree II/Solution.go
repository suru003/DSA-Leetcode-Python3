/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

package main

import "fmt"

func replaceValueInTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }

    queue := [][][]*TreeNode{{{root}}}

    for len(queue) > 0 {
        curLevel := queue[0]
        queue = queue[1:]

        total := 0
        for _, siblings := range curLevel {
            for _, node := range siblings {
                total += node.Val
            }
        }

        nextLevel := [][]*TreeNode{}
        for _, siblings := range curLevel {
            siblingsTotal := 0
            for _, node := range siblings {
                siblingsTotal += node.Val
            }

            for _, node := range siblings {
                node.Val = total - siblingsTotal
                children := []*TreeNode{}

                if node.Left != nil {
                    children = append(children, node.Left)
                }
                if node.Right != nil {
                    children = append(children, node.Right)
                }

                if len(children) > 0 {
                    nextLevel = append(nextLevel, children)
                }
            }
        }

        // Add next level nodes to the queue as lists of lists
        if len(nextLevel) > 0 {
            queue = append(queue, nextLevel)
        }
    }

    return root
}

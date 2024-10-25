type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}


func flipEquiv(root1 *TreeNode, root2 *TreeNode) bool {
    return dfs(root1, root2) && dfs(root2, root1)
}

func dfs(ptr1 *TreeNode, ptr2 *TreeNode) bool {
    if (ptr1 != nil && ptr2 == nil) || (ptr2 != nil && ptr1 == nil) {
        return false
    }
    if ptr1 == nil && ptr2 == nil {
        return true
    }
    if ptr1.Val != ptr2.Val {
        return false
    }

    valid := true

    if ptr1.Left != nil {
        if ptr2.Left != nil && ptr2.Left.Val == ptr1.Left.Val {
            valid = valid && dfs(ptr1.Left, ptr2.Left)
        } else if ptr2.Right != nil && ptr2.Right.Val == ptr1.Left.Val {
            valid = valid && dfs(ptr1.Left, ptr2.Right)
        } else {
            return false
        }
    }

    if ptr1.Right != nil {
        if ptr2.Left != nil && ptr2.Left.Val == ptr1.Right.Val {
            valid = valid && dfs(ptr1.Right, ptr2.Left)
        } else if ptr2.Right != nil && ptr2.Right.Val == ptr1.Right.Val {
            valid = valid && dfs(ptr1.Right, ptr2.Right)
        } else {
            return false
        }
    }

    return valid
}
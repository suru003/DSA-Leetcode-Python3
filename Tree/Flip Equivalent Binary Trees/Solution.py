"""
Link: https://leetcode.com/problems/flip-equivalent-binary-trees/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(ptr1, ptr2):
            if (ptr1 and not ptr2) \
                    or (ptr2 and not ptr1):
                return False

            if not (ptr1 or ptr2):
                return True

            if ptr1.val != ptr2.val:
                return False

            valid = True

            if ptr1.left:
                if ptr2.left and ptr2.left.val == ptr1.left.val:
                    valid &= dfs(ptr1.left, ptr2.left)
                elif ptr2.right and ptr2.right.val == ptr1.left.val:
                    valid &= dfs(ptr1.left, ptr2.right)
                else:
                    return False

            if ptr1.right:
                if ptr2.left and ptr2.left.val == ptr1.right.val:
                    valid &= dfs(ptr1.right, ptr2.left)
                elif ptr2.right and ptr2.right.val == ptr1.right.val:
                    valid &= dfs(ptr1.right, ptr2.right)
                else:
                    return False

            return valid

        return dfs(root1, root2) & dfs(root2, root1)

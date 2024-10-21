"""
Link: https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/
Time Complexity: O(nlogn)
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
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        tree_sizes = []

        def recurse(current):
            if not current:
                return 0

            left = recurse(current.left)
            right = recurse(current.right)

            if left != -1 and left == right:
                tree_sizes.append(left + right + 1)
                return left + right + 1

            return -1

        recurse(root)
        tree_sizes.sort()

        return -1 if k > len(tree_sizes) else tree_sizes[-k]

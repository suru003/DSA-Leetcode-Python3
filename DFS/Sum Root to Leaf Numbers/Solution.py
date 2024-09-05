'''
Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
Time Complexity: O(n)
Space Complexity: O(n) - stack space
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(current, val):
            if not current: return 0
            if not (current.left or current.right):
                return val * 10 + current.val
            else:
                return dfs(current.left, val * 10 + current.val) \
                       + dfs(current.right, val * 10 + current.val)

        return dfs(root, 0)

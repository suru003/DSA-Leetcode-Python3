'''
Link: https://leetcode.com/problems/diameter-of-binary-tree/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.getAns(root)
        return self.ans

    def getAns(self, root):
        if not root:
            return 0

        left = self.getAns(root.left)
        right = self.getAns(root.right)

        self.ans = max(self.ans, left + right)
        return max(left, right) + 1

"""
Link: https://leetcode.com/problems/cousins-in-binary-tree-ii/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque()
        dq.append([[root]])

        while dq:
            total = 0
            cur_level = dq.popleft()

            for siblings in cur_level:
                for node in siblings:
                    total += node.val

            next_level = []

            for siblings in cur_level:
                siblings_total = 0

                for node in siblings:
                    siblings_total += node.val

                for node in siblings:
                    node.val = total - siblings_total
                    children = []

                    if node.left:
                        children.append(node.left)
                    if node.right:
                        children.append(node.right)

                    if children:
                        next_level.append(children)

            if next_level:
                dq.append(next_level)

        return root

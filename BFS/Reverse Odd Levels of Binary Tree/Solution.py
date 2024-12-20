"""
Link: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([[[root], True]])

        while dq:
            level, flag = dq.popleft()
            next_level = []

            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if flag:
                for index in range(len(next_level) // 2):
                    left, right = next_level[index], next_level[-index - 1]
                    left.val, right.val = right.val, left.val

            if next_level:
                dq.append([next_level, not flag])

        return root

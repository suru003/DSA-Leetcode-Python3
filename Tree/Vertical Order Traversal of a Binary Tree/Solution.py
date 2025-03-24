"""
Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
Time Complexity: O(nlog(n))
Space Complexity: O(n)
"""
from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        left = right = 0
        mapped = defaultdict(dict)

        def traverse(current, row, col):
            if not current:
                return

            if row not in mapped[col]:
                mapped[col][row] = []

            mapped[col][row].append(current.val)
            traverse(current.left, row + 1, col - 1)
            traverse(current.right, row + 1, col + 1)

        traverse(root, 0, 0)
        answer = []

        for col_key in sorted(mapped.keys()):
            current_col = []
            for row_key in sorted(mapped[col_key].keys()):
                current_col.extend(sorted(mapped[col_key][row_key]))

            answer.append(current_col)

        return answer

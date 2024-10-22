"""
Link: https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/
Time Complexity: O(nlogn)
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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        dq = deque([[root]])
        sums = []

        while dq:
            current_level = dq.popleft()
            next_level = []
            cur_sum = 0

            for node in current_level:
                cur_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            sums.append(cur_sum)
            if next_level:
                dq.append(next_level)

        sums.sort(reverse=True)
        return -1 if len(sums) < k else sums[k - 1]

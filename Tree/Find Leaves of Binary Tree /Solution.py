'''
Link: https://leetcode.com/problems/find-leaves-of-binary-tree/
Link: https://www.lintcode.com/problem/650/
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """

    def findLeaves(self, root):
        leaves = []

        def recurse(cur):
            if not cur:
                return 0

            child = max(recurse(cur.left), recurse(cur.right))
            if len(leaves) <= child:
                leaves.append([])
            leaves[child].append(cur.val)

            return child + 1

        recurse(root)
        return leaves

'''
Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
Time Complexity: O(n)
Space Complexity: O(n)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        dq = deque()
        dq.append([root, None])

        while dq:
            curLevel = dq.popleft()
            dq.append([])

            for i in range(len(curLevel)):
                if curLevel[i]:
                    curLevel[i].next = curLevel[i + 1]

                    if curLevel[i].left:
                        dq[-1].append(curLevel[i].left)
                    if curLevel[i].right:
                        dq[-1].append(curLevel[i].right)

            if not dq[-1]: break
            dq[-1].append(None)

        return root

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        dq = deque([[root]])

        while dq:
            curr_level, next_level = dq.popleft(), []

            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            for ind in range(len(next_level) - 1):
                next_level[ind].next = next_level[ind + 1]

            if next_level:
                dq.append(next_level)

        return root

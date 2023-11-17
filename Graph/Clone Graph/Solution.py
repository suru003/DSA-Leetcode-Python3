'''
Link: https://leetcode.com/problems/clone-graph/
Time Complexity: O(n)
Space Complexity: O(n)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def cloneIt(node):
            if not node:
                return None

            clone = Node(node.val)
            visited[node.val] = clone

            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    clone.neighbors.append(cloneIt(neighbor))
                else:
                    clone.neighbors.append(visited[neighbor.val])

            return clone

        return cloneIt(node)

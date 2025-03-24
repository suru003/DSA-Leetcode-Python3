from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]
        while (root.left):
            self.stack.append(root.left)
            root = root.left

    def next(self) -> int:
        nextNode = self.stack.pop()

        if (nextNode.right):
            self.stack.append(nextNode.right)
            temp = nextNode.right

            while (temp.left):
                self.stack.append(temp.left)
                temp = temp.left

        return nextNode.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
'''
Link: https://leetcode.com/problems/lru-cache/
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Node:
    def __init__(self, key, val, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # delete node
        node.left.right = node.right
        node.right.left = node.left

        # add to end
        self.tail.left.right = node
        node.left = self.tail.left
        node.right = self.tail
        self.tail.left = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key)
            self.cache[key].val = value
            return

        elif self.cap == len(self.cache):
            toRemove = self.head.right
            self.cache.pop(toRemove.key)
            self.head.right = toRemove.right
            toRemove.right.left = self.head

        node = Node(key, value)
        self.cache[key] = node

        # add to end
        self.tail.left.right = node
        node.left = self.tail.left
        node.right = self.tail
        self.tail.left = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
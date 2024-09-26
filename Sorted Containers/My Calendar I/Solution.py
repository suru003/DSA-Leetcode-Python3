'''
Link: https://leetcode.com/problems/my-calendar-i/
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None


class MyCalendar:
    def __init__(self):
        self.root = None

    def dfs(self, start, end, ptr):
        if not ptr:
            ptr = Node(start, end)

            if not self.root:
                self.root = ptr

            return True

        # `ptr` is starting after the `end` for insert
        if ptr.start >= end:
            if not ptr.left:
                ptr.left = Node(start, end)
                return True

            return self.dfs(start, end, ptr.left)

        # `ptr` is ended before the `start` for insert
        elif ptr.end <= start:
            if not ptr.right:
                ptr.right = Node(start, end)
                return True

            return self.dfs(start, end, ptr.right)

        return False

    def book(self, start: int, end: int) -> bool:
        return self.dfs(start, end, self.root)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

"""
Link: https://leetcode.com/problems/basic-calculator/
Time Complexity: O(1)
Space Complexity: O(n)
"""


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.limit = maxSize

    def push(self, x: int) -> None:
        if self.limit == len(self.stack):
            return

        self.stack.append({'val': x, 'offsets': []})

    def pop(self) -> int:
        if not self.stack:
            return -1

        last = self.stack.pop()
        to_return = last['val']
        for offset, k in last['offsets']:
            if k > 0:
                if self.stack:
                    self.stack[-1]['offsets'].append([offset, k - 1])

                to_return += offset

        return to_return

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return

        if len(self.stack) < k:
            self.stack[-1]['offsets'].append([val, k])
        else:
            self.stack[k - 1]['offsets'].append([val, k])

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
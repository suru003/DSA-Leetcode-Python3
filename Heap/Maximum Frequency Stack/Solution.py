"""
Link: https://leetcode.com/problems/maximum-frequency-stack/
Time Complexity: O(Logn) For Push and O(Logn) For Pop
Space Complexity: O(n)
"""
import heapq as hq
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.counts = defaultdict(int)
        self.heap = []
        self.counter = 0

    def push(self, val: int) -> None:
        self.counts[val] -= 1
        self.counter -= 1
        hq.heappush(self.heap, [self.counts[val], self.counter, val])

    def pop(self) -> int:
        while self.heap and \
        self.heap[0][0] != self.counts[self.heap[0][2]]:
            hq.heappop(self.heap)

        count, _, val = hq.heappop(self.heap)
        self.counts[val] += 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
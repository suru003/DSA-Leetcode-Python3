"""
Link: https://leetcode.com/problems/snapshot-array/
Time Complexity: Different for each function
Space Complexity: O(n) whole
"""

from bisect import bisect_right

class SnapshotArray:
    def __init__(self, length: int):
        self.snaps = -1
        self.array = {}
        for i in range(length):
            self.array[i] = [[-1, 0]]

    def set(self, index: int, val: int) -> None:
        if self.array[index][0] == self.snaps:
            self.array[index][1] = val
        else:
            self.array[index].append([self.snaps, val])

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps

    def get(self, index: int, snap_id: int) -> int:
        pos = bisect_right(self.array[index], [snap_id, 0]) - 1
        return self.array[index][pos][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
"""
Link: https://leetcode.com/problems/find-median-from-data-stream/
Time Complexity: O(nlog(n))
Space Complexity: O(n)
"""
from sortedcontainers import SortedList


class MedianFinder:
    def __init__(self):
        self.sorted_list = SortedList()

    def addNum(self, num: int) -> None:
        self.sorted_list.add(num)

    def findMedian(self) -> float:
        n = len(self.sorted_list)
        mid = n >> 1

        if n % 2:
            return self.sorted_list[mid]

        return (self.sorted_list[mid] + self.sorted_list[mid - 1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
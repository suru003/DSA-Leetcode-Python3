'''
Link: https://leetcode.com/problems/employee-free-time/
Link: https://www.lintcode.com/problem/850/
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from typing import List

class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals
    """

    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        schedules = []
        for sc in schedule:
            for i in range(0, len(sc), 2):
                schedules.append([sc[i], sc[i + 1]])

        schedules.sort()
        stack = []

        for a, b in schedules:
            if stack and stack[-1][1] >= a:
                stack[-1][1] = max(stack[-1][1], b)
            else:
                stack.append([a, b])

        free = []
        for i in range(len(stack) - 1):
            free.append(Interval(stack[i][1], stack[i + 1][0]))

        return free

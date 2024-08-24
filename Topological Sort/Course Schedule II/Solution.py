"""
Link: https://leetcode.com/problems/course-schedule-ii/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = defaultdict(int)

        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1

        q = []

        for course in range(numCourses):
            if not indegrees[course]:
                q.append(course)

        order = []

        while q:
            current = q.pop()
            order.append(current)
            for next_course in graph[current]:
                indegrees[next_course] -= 1
                if not indegrees[next_course]:
                    q.append(next_course)

        return order if len(order) == numCourses else []

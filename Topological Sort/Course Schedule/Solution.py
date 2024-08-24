"""
Link: https://leetcode.com/problems/course-schedule/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = defaultdict(int)

        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1

        q = []

        for course in range(numCourses):
            if not indegrees[course]:
                q.append(course)

        finished = 0

        while q:
            current = q.pop()
            finished += 1
            for next_course in graph[current]:
                indegrees[next_course] -= 1
                if not indegrees[next_course]:
                    q.append(next_course)

        return finished == numCourses

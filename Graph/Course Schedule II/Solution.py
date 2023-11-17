'''
Link: https://leetcode.com/problems/course-schedule-ii/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        willOpen = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        for course, preReq in prerequisites:
            indegree[course] += 1
            willOpen[preReq].append(course)

        dq = deque()

        for index in range(numCourses):
            if not indegree[index]:
                dq.append(index)

        order = []
        while dq:
            complete = dq.popleft()
            order.append(complete)

            for course in willOpen[complete]:
                indegree[course] -= 1
                if not indegree[course]:
                    dq.append(course)

        return order if len(order) == numCourses else []

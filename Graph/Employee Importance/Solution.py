'''
Link: https://leetcode.com/problems/employee-importance/
Time Complexity: O(n)
Space Complexity: O(n)
'''
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from typing import List
from collections import deque

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total = 0
        dq = deque()
        dq.append(id)

        id_map = {employees[i].id: i for i in range(len(employees))}

        while dq:
            current = dq.popleft()
            total += employees[id_map[current]].importance

            for subs in employees[id_map[current]].subordinates:
                dq.append(subs)

        return total

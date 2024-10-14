"""
Link: https://leetcode.com/contest/weekly-contest-371/problems/high-access-employees/
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
from collections import defaultdict
from typing import List
import heapq as hq

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        accesses = defaultdict(list)
        oneHour = 60

        def getMinutes(time):
            return oneHour * int(time[:2]) + int(time[2:])

        for name, time in access_times:
            accesses[name].append(getMinutes(time))

        answers = []

        for name in accesses.keys():
            sortedAccesses = sorted(accesses[name])
            currentWindow = []
            for access in sortedAccesses:
                while currentWindow and access - currentWindow[0] >= oneHour:
                    hq.heappop(currentWindow)

                hq.heappush(currentWindow, access)

                if len(currentWindow) == 3:
                    answers.append(name)
                    break

        return answers

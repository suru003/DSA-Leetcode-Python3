'''
Link: https://leetcode.com/contest/weekly-contest-370/problems/maximum-score-after-applying-operations-on-a-tree/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List
from collections import defaultdict

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        tree = defaultdict(list)

        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def recurse(cur, parent):
            if len(tree[cur]) == 1 and tree[cur][0] == parent:
                return values[cur]

            total_min = 0
            for child in tree[cur]:
                if child != parent:
                    total_min += recurse(child, cur)

            return min(total_min, values[cur])

        total = sum(values)
        return total - recurse(0, -1)

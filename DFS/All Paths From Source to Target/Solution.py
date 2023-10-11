'''
Link: https://leetcode.com/problems/all-paths-from-source-to-target/
Time Complexity: O(2^n)
Space Complexity: O(V)
'''
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans, n = [], len(graph)

        def dfs(cur, path):
            if cur == n - 1:
                ans.append(path)

            for adj in graph[cur]:
                dfs(adj, path + [adj])

        dfs(0, [0])
        return ans

'''
Link: https://leetcode.com/problems/possible-bipartition/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List
from collections import defaultdict


# Solution is check if the graph contains any even length cycle

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colored = defaultdict(int)
        graph = defaultdict(list)
        BLUE, GREEN = 1, -1

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(cur, parent, color):
            for adj in graph[cur]:
                if adj == parent:
                    continue

                # To return False in case of same colors
                if adj in colored and colored[adj] == color:
                    return False

                elif adj not in colored:
                    colored[adj] = -color
                    dfs(adj, cur, -color)

            return True

        for i in range(1, n + 1):
            colored[i] = colored.get(i, BLUE)
            valid = dfs(i, -1, colored[i])
            if not valid:
                return valid

        return True

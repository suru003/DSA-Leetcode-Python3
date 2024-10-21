"""
Link: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/
Time Complexity: O(n log K + n log X)
Space Complexity: O(n)
"""
from typing import List
from collections import Counter
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, A: List[int], K: int, X: int) -> List[int]:
        rem = SortedList()
        topX = SortedList()
        count = Counter()
        cur_sum = 0

        def update(x, qty):
            nonlocal cur_sum

            if count[x]:
                try:
                    rem.remove([count[x], x])
                except:
                    topX.remove([count[x], x])
                    cur_sum -= count[x] * x

            count[x] += qty
            if count[x]:
                rem.add([count[x], x])

        ans = []
        for i in range(len(A)):
            update(A[i], 1)
            if i >= K:
                update(A[i - K], -1)

            # rebalance
            while rem and len(topX) < X:
                cx, x = rem.pop()
                cur_sum += cx * x
                topX.add([cx, x])

            while rem and rem[-1] > topX[0]:
                cx, x = rem.pop()
                cy, y = topX.pop(0)
                cur_sum += cx * x - cy * y
                rem.add([cy, y])
                topX.add([cx, x])

            if i >= K - 1:
                ans.append(cur_sum)

        return ans
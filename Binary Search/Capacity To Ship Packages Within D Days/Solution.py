'''
Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
Time Complexity: O(nlog(sum(weights) - max(weights)))
Space Complexity: O(1)
'''
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        def isPossible(lim):
            cnt, temp = 1, 0
            for w in weights:
                if w + temp <= lim:
                    temp = w + temp
            else:
                temp = w
                cnt += 1
            if cnt > days:
                return False

            return True

        while low <= high:
            mid = (low + high) >> 1
            if isPossible(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low

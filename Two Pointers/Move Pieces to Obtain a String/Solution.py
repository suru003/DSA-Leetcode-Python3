"""
Link: https://leetcode.com/problems/move-pieces-to-obtain-a-string/
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        start_ptr = 0
        target_ptr = 0

        while target_ptr < n:
            while target_ptr < n and target[target_ptr] == '_':
                target_ptr += 1

            while start_ptr < n and start[start_ptr] == '_':
                start_ptr += 1

            if start_ptr < n and target_ptr < n:
                if target[target_ptr] != start[start_ptr]:
                    return False

                if target[target_ptr] == 'L' and start_ptr < target_ptr:
                    return False

                if target[target_ptr] == 'R' and start_ptr > target_ptr:
                    return False

            start_ptr += 1
            target_ptr += 1

        return start.count('L') == target.count('L') \
            and start.count('R') == target.count('R')

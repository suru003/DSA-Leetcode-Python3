"""
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_gcd(a, b):
            if a < b:
                a, b = b, a

            while b:
                a, b = b, a % b

            return a

        ptr = head

        while ptr.next:
            gcd = get_gcd(ptr.val, ptr.next.val)
            ptr.next = ListNode(gcd, ptr.next)
            ptr = ptr.next.next

        return head

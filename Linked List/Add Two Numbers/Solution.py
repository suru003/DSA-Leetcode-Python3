"""
Link: https://leetcode.com/problems/add-two-numbers/
Time Complexity: O((n+m)
Space Complexity: O(n)
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1

        def recurse(ptr1, ptr2, carry):
            if not (ptr1 or ptr2 or carry):
                return None

            total, carry = carry, 0
            if ptr1:
                total += ptr1.val

            if ptr2:
                total += ptr2.val

            if ptr1 and ptr2:
                return ListNode(total % 10, recurse(ptr1.next, ptr2.next, total // 10))
            elif ptr1:
                return ListNode(total % 10, recurse(ptr1.next, None, total // 10))
            elif ptr2:
                return ListNode(total % 10, recurse(None, ptr2.next, total // 10))

            return ListNode(total % 10, recurse(None, None, total // 10))

        return recurse(l1, l2, 0)

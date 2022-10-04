"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

from typing import Optional
from common.list import ListNode

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        curr = head
        next = head.next

        while next is not None:
            if curr.val == next.val:
                next = next.next
            else:
                curr.next = next
                curr = next
                next = next.next

        curr.next = next
        return head







"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

from typing import Optional
from common.list import ListNode

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: 
            return False
        s = []
        while head:
            s += str(head.val)
            head = head.next
        return s == s[::-1]
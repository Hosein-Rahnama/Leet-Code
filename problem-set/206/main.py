# 206. Reverse Linked List

from typing import Optional, List
from lib.LinkedList import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None):
            return head
        
        previous = None
        current = head
        next = head.next
        while (current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        return previous

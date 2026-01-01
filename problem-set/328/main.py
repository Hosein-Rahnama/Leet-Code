# 328. Odd Even Linked List

from typing import Optional
from lib.LinkedList import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None):
            return None
            
        even_head = head.next

        odd = head
        even = odd.next
        while ((even is not None) and (even.next is not None)):
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd_tail = odd
        odd_tail.next = even_head
        
        return head

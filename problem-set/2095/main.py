# 2095. Delete the Middle Node of a Linked List

from typing import Optional
from lib.LinkedList import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = get_length(head)
        if (n <= 1):
            return None
        
        m = n // 2
        node = head
        for _ in range(m - 1):
            node = node.next
        prev = node
        node = node.next

        prev.next = node.next
        node.next = None

        return head

def get_length(head: Optional[ListNode]) -> int:
    n = 0
    node = head
    while (node is not None):
        n += 1
        node = node.next
    return n

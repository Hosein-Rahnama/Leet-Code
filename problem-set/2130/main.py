# 2130. Maximum Twin Sum of a Linked List

from typing import Optional
from lib.LinkedList import ListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        middle = head
        node = head
        while (node is not None):
            node = node.next.next
            middle = middle.next

        back = None
        node = middle
        while (node is not None):
            front = node.next
            node.next = back
            back = node
            node = front

        max_sum = 0
        last = back
        first = head
        while (last is not None):
            max_sum = max(max_sum, first.val + last.val)
            first = first.next
            last = last.next

        return max_sum

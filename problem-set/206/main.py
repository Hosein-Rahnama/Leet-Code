# 206. Reverse Linked List

from typing import Optional, List
from lib.LinkedList import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = get_values(head)
        last = make_list(values[::-1])
        return last

def get_values(head: Optional[ListNode]) -> List[int]:
    values = []
    node = head
    while (node is not None):
        values.append(node.val)
        node = node.next
    return values

def make_list(values: List[int]) -> ListNode:
    if len(values) == 0:
        return None

    head = ListNode(values[0])
    node = head
    for i in range(1, len(values)):
        node.next = ListNode(values[i])
        node = node.next
    return head

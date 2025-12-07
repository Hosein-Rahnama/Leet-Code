from typing import Optional, List


class ListNode:
    def __init__(self, val: int, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, *values: int):
        if len(values) == 0:
            self.head = None
            return
        
        self.head = ListNode(values[0])
        node = self.head
        for i in range(1, len(values)):
            node.next = ListNode(values[i])
            node = node.next

    @classmethod
    def from_head(self, head: ListNode) -> LinkedList:
        self.head = head
        values = []
        node = head
        while (node is not None):
            values.append(node.val)
            node = node.next
        return LinkedList(*values)
    
    def values(self) -> List[int]:
        values = []
        node = self.head
        while (node is not None):
            values.append(node.val)
            node = node.next
        return values

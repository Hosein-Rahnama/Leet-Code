from typing import Optional, List


class LinkedList:
    pass

class ListNode:
    def __init__(self, val: int, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(LinkedList.from_head(self))

class LinkedList:
    def __init__(self, values: List[int] = []):
        if len(values) == 0:
            self.head = None
            return
        
        self.head = ListNode(values[0])
        node = self.head
        for i in range(1, len(values)):
            node.next = ListNode(values[i])
            node = node.next

    @classmethod
    def from_head(cls, head: ListNode) -> LinkedList:
        l = LinkedList()
        l.head = head
        return l
    
    def values(self) -> List[int]:
        values = []
        node = self.head
        while (node is not None):
            values.append(node.val)
            node = node.next
        return values
    
    def __str__(self):
        string = map(str, self.values())
        string = ", ".join(string)
        return f"[{string}]"

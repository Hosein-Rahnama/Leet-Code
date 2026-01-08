from typing import Optional, List
from collections import deque


class BinaryTree():
    pass

class TreeNode:
    def __init__(self, val: int, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right
    
    def is_leaf(self):
        return (self.left is None) and (self.right is None)
    
    def __str__(self):
        return str(BinaryTree.from_root(self))

class BinaryTree:
    def __init__(self, values: List[int] = []):
        n = len(values)
        if n == 0:
            self.root = None
            return
        
        nodes = [(TreeNode(values[i]) if values[i] is not None else None) for i in range(n)]
        self.root = nodes[0]
        i = 0
        j = 1
        l = 1
        while (j < len(nodes)):
            count = 0
            u = i + l
            while (i < u):
                node = nodes[i]
                if (node is not None):
                    node.left = nodes[j]
                    node.right = nodes[j + 1]
                    j += 2
                    count += 1
                i += 1
            l = 2 * count

    @classmethod
    def from_root(cls, root: TreeNode) -> BinaryTree:
        t = BinaryTree()
        t.root = root
        return t
    
    def values(self) -> List[int]:
        root = self.root
        if (root is None):
            return []
        
        q = deque([root])
        values = [root.val]
        while (len(q) != 0):
            node = q.popleft()
            left = right = None
            if (node is not None):
                left = node.left
                right = node.right
                left_value = left.val if left is not None else None
                right_value = right.val if right is not None else None
                values.append(left_value)
                values.append(right_value)
            q.append(left)
            q.append(right)
                
        return values
    
    def __str__(self):
        string = map(str, self.values())
        string = ", ".join(string)
        return f"[{string}]"

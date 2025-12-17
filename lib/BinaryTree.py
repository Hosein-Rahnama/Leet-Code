from typing import Optional, List
from collections import deque
from math import log2


class BinaryTree():
    pass

class TreeNode:
    def __init__(self, val: int, left: Optional[TreeNode] = None, right:Optional[TreeNode] = None):
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
        h = int(log2(n + 1) - 1)
        for i in range(2 ** h - 1):
                node = nodes[i]
                if (node is not None):
                    node.left = nodes[2 * i + 1]
                    node.right = nodes[2 * i + 2]
            
    @classmethod
    def from_root(cls, root: TreeNode) -> BinaryTree:
        t = BinaryTree()
        t.root = root
        return t
    
    def height(self):
        root = self.root
        if ((root is None) or root.is_leaf()):
            return 0
        left = BinaryTree.from_root(root.left)
        right = BinaryTree.from_root(root.right)
        h = max(left.height(), right.height()) + 1
        return h
    
    def values(self) -> List[int]:
        root = self.root
        if (root is None):
            return []
        
        h = self.height()
        q = deque([root])
        values = [root.val]
        for _ in range(h):
            for _ in range(len(q)):
                node = q.popleft()
                left = right = None
                if (node is not None):
                    left = node.left
                    right = node.right
                q.append(left)
                q.append(right)
                
                left_value = left.val if left is not None else None
                right_value = right.val if right is not None else None
                values.append(left_value)
                values.append(right_value)
                
        return values
    
    def __str__(self):
        string = map(str, self.values())
        string = ", ".join(string)
        return f"[{string}]"

from typing import Optional, List
from math import log2
import queue


class TreeNode:
    def __init__(self, val: int, left: Optional[TreeNode] = None, right:Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

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
    
    def values(self) -> List[int]:
        if (self.root is None):
            return []
        
        values = []
        q = queue.Queue()
        q.put(self.root)
        while (not q.empty()):
            node = q.get()
            values.append(node.val)
            if node.left is not None:
                q.put(node.left) 
            if node.right is not None:
                q.put(node.right)   
                
        return values

# 872. Leaf-Similar Trees

from typing import Optional, List
from lib.BinaryTree import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = []
        get_leafs(root1, leafs1)
        leafs2 = []
        get_leafs(root2, leafs2)
        return leafs1 == leafs2

def get_leafs (node: Optional[TreeNode], values: List[int]):
    if (node is None):
        return
    
    get_leafs(node.left, values)
    get_leafs(node.right, values)
    is_leaf = (node.left is None) and (node.right is None)
    if is_leaf:
        values.append(node.val)

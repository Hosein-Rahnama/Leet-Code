# 872. Leaf-Similar Trees

from typing import Optional, List
from lib.BinaryTree import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = []
        get_leaves(root1, leafs1)
        leafs2 = []
        get_leaves(root2, leafs2)
        return leafs1 == leafs2

def get_leaves (node: Optional[TreeNode], values: List[int]):
    if (node is None):
        return
    if ((node.left is None) and (node.right is None)):
        values.append(node.val)
        return
    
    get_leaves(node.left, values)
    get_leaves(node.right, values)

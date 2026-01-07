# 872. Leaf-Similar Trees

from typing import Optional, List
from lib.BinaryTree import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return get_leaves(root1) == get_leaves(root2)

def get_leaves (node: Optional[TreeNode]) -> List[int]:
    if (node is None):
        return []
    if ((node.left is None) and (node.right is None)):
        return [node.val]
    
    left_leaves = get_leaves(node.left)
    right_leaves = get_leaves(node.right)

    return left_leaves + right_leaves

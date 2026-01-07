# 1448. Count Good Nodes in Binary Tree

from typing import Optional
from lib.BinaryTree import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return count_good(root, float("-inf"))

def count_good(root: Optional[TreeNode], max_node) -> int:
    if (root is None):
        return 0
    
    is_good = 1 if (root.val >= max_node) else 0

    max_node = max(root.val, max_node)
    left_count = count_good(root.left, max_node)
    right_count = count_good(root.right, max_node)

    return left_count + right_count + is_good

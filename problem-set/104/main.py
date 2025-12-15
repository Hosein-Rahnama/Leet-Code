# 104. Maximum Depth of Binary Tree

from typing import Optional
from lib.BinaryTree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0
        maxDepth = self.maxDepth
        height = max(maxDepth(root.left), maxDepth(root.right)) + 1
        return height
    
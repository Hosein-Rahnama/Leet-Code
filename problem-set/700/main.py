# 700. Search in a Binary Search Tree

from typing import Optional
from lib.BinaryTree import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if (root is None):
            return None

        if (val == root.val):
            return root
        elif (val < root.val):
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

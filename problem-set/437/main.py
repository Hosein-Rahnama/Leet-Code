# 437. Path Sum III

from typing import List, Optional
from lib.BinaryTree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        sums = dict()
        current_sum = 0
        count = Counter(0)
        dfs(root, target_sum, current_sum, sums, count)
        return count.value

def dfs(root: Optional[TreeNode], target_sum: int, current_sum: int, sums: List[int], count: Counter):
    if (root is None):
        return
    
    current_sum += root.val
    old_sum = current_sum - target_sum
    count.value += sums.get(old_sum, 0)
    if (old_sum == 0):
        count.value += 1
    sums[current_sum] = sums.get(current_sum, 0) + 1

    dfs(root.left, target_sum, current_sum, sums, count)
    dfs(root.right, target_sum, current_sum, sums, count)
    
    sums[current_sum] -= 1

class Counter():
    def __init__(self, value):
        self.value = value

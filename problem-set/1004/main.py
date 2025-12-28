# 1004. Max Consecutive Ones III

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_width = 0
        num_zeros = 1 if (nums[0] == 0) else 0
        start = end = 0
        while (end < n):
            if (num_zeros <= k):
                end += 1
                if (end < n and nums[end] == 0):
                    num_zeros += 1
            else:
                if (nums[start] == 0):
                    num_zeros -= 1
                start += 1
            max_width = max(max_width, end - start)
        
        return max_width

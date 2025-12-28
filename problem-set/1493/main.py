# 1493. Longest Subarray of 1's After Deleting One Element

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        num_zeros = 0
        start = end = 0
        while (end < n):
            if (nums[end] == 0):
                num_zeros += 1
            if (num_zeros > k):
                num_zeros -= 1 if (nums[start] == 0) else 0
                start += 1
            end += 1
        
        return end - start - 1

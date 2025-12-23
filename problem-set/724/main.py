# 724. Find Pivot Index

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = 0
        right_sum = 0
        for i in range(1, n):
            right_sum += nums[i]

        for i in range(n):
            if (left_sum == right_sum):
                return i
            left_sum += nums[i]
            if (i <= n - 2):
                right_sum -= nums[i + 1]

        return -1

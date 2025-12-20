# 238. Product of Array Except Self

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_product = [0 for _ in range(n)]
        left_product[0] = 1
        for i in range(1, n):
            left_product[i] = nums[i - 1] * left_product[i - 1]

        right_product = [0 for _ in range(n)]
        right_product[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right_product[i] = nums[i + 1] * right_product[i + 1]

        product = [0 for _ in range(n)]
        for i in range(n):
            product[i] = left_product[i] * right_product[i]

        return product

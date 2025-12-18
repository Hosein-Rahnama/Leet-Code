# 136. Single Number

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_xor = 0
        for i in nums:
            nums_xor ^= i
        return nums_xor

# 11. Container With Most Water

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max = 0
        while (left < right):
            c = capacity(left, right, height)
            if (c > max):
                max = c
            if (height[left] <= height[right]):
                left += 1
            else:
                right -= 1
        return max

def capacity(left, right, height):
    h = min(height[left], height[right])
    c = (right - left) * h
    return c

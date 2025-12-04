# 643. Maximum Average Subarray I

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = 0.0
        for i in range(k):
            max_avg += nums[i]
        max_avg /= k

        avg = max_avg
        for i in range(len(nums) - k):
            avg += (-nums[i] + nums[i + k]) / k
            if (avg > max_avg):
                max_avg = avg
        
        return max_avg

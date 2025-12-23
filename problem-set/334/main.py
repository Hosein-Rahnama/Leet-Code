# 334. Increasing Triplet Subsequence

class Solution:
    def increasingTriplet(self, nums):
        n = len(nums)

        prefix_min = [0 for _ in range(n)]
        min = nums[0]
        for i in range(n):
            if (nums[i] < min):
                min = nums[i]
            prefix_min[i] = min

        suffix_max = [0 for _ in range(n)]
        max = nums[-1]
        for i in range(n - 1, -1, -1):
            if (nums[i] > max):
                max = nums[i]
            suffix_max[i] = max

        for i in range(n):
            if (prefix_min[i] < nums[i] < suffix_max[i]):
                return True
            
        return False

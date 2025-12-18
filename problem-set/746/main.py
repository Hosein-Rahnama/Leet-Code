# 746. Min Cost Climbing Stairs

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost = [0 for _ in range(n + 1)]

        min_cost[0] = 0
        min_cost[1] = 0
        for i in range(2, n + 1):
            min_cost[i] = min(min_cost[i - 1] + cost[i - 1], min_cost[i - 2] + cost[i - 2])

        return min_cost[n]

# 1431. Kids With the Greatest Number of Candies

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        checkList = [False for _ in range(n)]
        for kid in range(n):
            candies[kid] += extraCandies
            if hasMostCandies(kid, candies):
                checkList[kid] = True
            candies[kid] -= extraCandies
        return checkList


def hasMostCandies(kid: int, candies: List[int]) -> bool:
    n = len(candies)
    for i in range(n):
        if candies[kid] < candies[i]:
            return False
    return True

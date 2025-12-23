# 1431. Kids With the Greatest Number of Candies

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extra: int) -> List[bool]:
        n = len(candies)
        check_list = [False for _ in range(n)]
        for kid in range(n):
            candies[kid] += extra
            if has_most_candies(kid, candies):
                check_list[kid] = True
            candies[kid] -= extra
        return check_list


def has_most_candies(kid: int, candies: List[int]) -> bool:
    n = len(candies)
    for i in range(n):
        if candies[kid] < candies[i]:
            return False
    return True

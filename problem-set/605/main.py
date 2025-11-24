# 605. Can Place Flowers

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        free_places = [1 for _ in range(m)]

        for i in range(m):
            if flowerbed[i] == 1:
                occupy_bed(i, free_places)
        
        cnt = 0
        for i in range(m):
            if (free_places[i] == 1):
                cnt += 1
                occupy_bed(i, free_places)
        
        is_possible = True if (n <= cnt) else False
        return is_possible


def occupy_bed(i: int, free_places: List[int]) -> None:
    m = len(free_places)

    if (m == 1):
        free_places[i] = 0
        return

    if (0 < i < (m - 1)):
        free_places[i - 1] = 0
        free_places[i] = 0
        free_places[i + 1] = 0
    elif (i == 0):
        free_places[i] = 0
        free_places[i + 1] = 0
    else:
        free_places[i - 1] = 0
        free_places[i] = 0

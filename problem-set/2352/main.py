# 2352. Equal Row and Column Pairs

from typing import List
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_freq = Counter(map(tuple, grid))
        col_freq = Counter(zip(*grid))
        sum = 0
        for r in row_freq.keys():
            sum += row_freq[r] * col_freq[r]
        
        return sum

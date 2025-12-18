# 338. Counting Bits

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        a = [0 for _ in range(n + 1)]
        for i in range(n + 1):
            a[i] = a[i // 2] + (i % 2)
        return a

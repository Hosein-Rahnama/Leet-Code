# 1207. Unique Number of Occurrences

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = {}
        for i in arr:
            occur[i] = occur.get(i, 0) + 1

        if len(occur.values()) == len(set(occur.values())):
            return True
        
        return False

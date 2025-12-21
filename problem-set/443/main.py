# 443. String Compression

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        j = 0
        while (i < n):
            char = chars[i]
            count = 0
            while (i < n and char == chars[i]):
                count += 1
                i += 1
            chars[j] = char
            j += 1
            if (count > 1):
                count = str(count)
                for digit in count:
                    chars[j] = digit
                    j += 1
        return j

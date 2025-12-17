# 374. Guess Number Higher or Lower

from random import randint


class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n
        while (True):
            num = ((end + start) // 2) + randint(0, 1)
            state = guess(num)
            if (state == 0):
                break
            elif (state == -1):
                end = num
            else:
                start = num
        return num

# 2390. Removing Stars From a String

from collections import deque


class Solution:
    def removeStars(self, string: str) -> str:
        stack = deque([])
        for char in string:
            if (char != "*"):
                stack.append(char)
            else:
                stack.pop()

        new_string = ""
        for char in stack:
            new_string += char

        return new_string

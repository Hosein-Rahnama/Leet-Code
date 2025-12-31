# 394. Decode String

from collections import deque


class Solution:
    def decodeString(self, string: str) -> str:
        stack = deque([]) 
        for char in string:
            if (char != "]"):
                stack.append(char)
            else:
                code = ""
                while (stack[-1] != "["):
                    code = stack.pop() + code
                stack.pop()

                n = ""
                while ((len(stack) != 0) and stack[-1].isdigit()):
                    n = stack.pop() + n
                n = int(n)

                stack.append(n * code)

        decoded = ""
        while (len(stack) != 0):
            decoded = stack.pop() + decoded
        
        return decoded

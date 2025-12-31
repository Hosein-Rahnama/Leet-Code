# 735. Asteroid Collision

from typing import List
from collections import deque


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque([])
        for mass in asteroids:
            mass_destroyed = False
            while ((len(stack) != 0) and (mass < 0 and stack[-1] > 0)):
                if (-mass > stack[-1]):
                    stack.pop()
                elif (-mass == stack[-1]):
                    stack.pop()
                    mass_destroyed = True
                    break
                else:
                    mass_destroyed = True
                    break
                
            if (not mass_destroyed):
                stack.append(mass)
        
        return list(stack)

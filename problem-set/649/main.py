# 649. Dota2 Senate

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        dire = [i for i in range(n) if (senate[i] == "D")]
        dire = deque(dire)
        radiant = [i for i in range(n) if (senate[i] == "R")]
        radiant = deque(radiant)

        while (len(dire) > 0 and len(radiant) > 0):
            dire_senator = dire.popleft()
            radiant_senator = radiant.popleft()
            if (dire_senator < radiant_senator):
                dire.append(dire_senator + n)
            else:
                radiant.append(radiant_senator + n)

        winner = "Dire" if (len(dire) > len(radiant)) else "Radiant"
        return winner

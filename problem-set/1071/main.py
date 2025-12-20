# 1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, string1: str, string2: str) -> str:
        if (string1 + string2 != string2 + string1):
            return ""

        d = gcd(len(string1), len(string2))
        pattern = string1[0: d]
        
        return pattern
    

def gcd(n: int, m: int) -> int:
    if m > n:
        n, m = m, n

    r = 1
    while (r != 0):
        r = n % m
        n = m
        m = r
    return n

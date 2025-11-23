# 1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, string1: str, string2: str) -> str:
        n1 = len(string1)
        n2 = len(string2)

        d = GCD(n1, n2)
        if (string1[0:d] != string2[0:d]):
            return ""
        
        pattern = string1[0:d]
        if not (isStringDivisor(pattern, string1) and isStringDivisor(pattern, string2)):
            return ""
        
        return pattern
    

def GCD(n: int, m: int) -> int:
    r = 1
    if m > n:
        n, m = m, n
    while (r != 0):
        r = n % m
        n = m
        m = r
    return n
    
    
def isStringDivisor(pattern: str, string: str) -> bool:
    d = len(pattern)
    n = len(string)
    if (n % d != 0):
        return False
    
    q = n // d
    for i in range(q):
        start = i * d
        end = (i + 1) * d
        if pattern != string[start:end]:
            return False
    
    return True  

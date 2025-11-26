# 1768. Merge Strings Alternately

class Solution:    
    def mergeAlternately(self, string1: str, string2: str) -> str:
        merged_string = ""
        n1 = len(string1)
        n2 = len(string2)
        l = min(n1, n2)

        for i in range(l):
            merged_string += string1[i] + string2[i]
        for i in range(l, n1):
            merged_string += string1[i]
        for i in range(l, n2):
            merged_string += string2[i]

        return merged_string

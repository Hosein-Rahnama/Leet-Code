# 1768. Merge Strings Alternately

class Solution:    
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        n1 = len(word1)
        n2 = len(word2)
        l = min(n1, n2)

        for i in range(l):
            merged_word = merged_word + word1[i] + word2[i]
        for i in range(l, n1):
            merged_word += word1[i]
        for i in range(l, n2):
            merged_word += word2[i]

        return merged_word

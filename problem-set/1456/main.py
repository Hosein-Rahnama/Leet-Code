# 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        count = 0
        for i in range(k):
            if (s[i] in vowels):
                count += 1

        max_vowels = count
        for i in range(k, len(s)):
            if (s[i - k] in vowels):
                count -= 1
            if (s[i] in vowels):
                count += 1
            if (count > max_vowels):
                max_vowels = count

        return max_vowels

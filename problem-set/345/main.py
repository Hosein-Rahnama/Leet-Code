# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, string: str) -> str:
        vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
        string_vowels = []
        
        for c in string:
            if (c in vowels):
                string_vowels.append(c)

        new_string = ""
        for c in string:
            if (c not in vowels):
                new_string += c
            else:
                new_string += string_vowels.pop()

        return new_string

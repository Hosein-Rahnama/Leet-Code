# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, string: str) -> str:
        words = get_tokens(string)
        words = words[::-1]
        reversed_string = " ".join(words)
        return reversed_string

def get_tokens(string: str):
    tokens = []
    string += " "
    word = ""
    for char in string:
        if char == " ":
            if (word != ""):
                tokens.append(word)
                word = ""
            continue
        word += char

    return tokens

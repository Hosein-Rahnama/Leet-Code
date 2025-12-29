# 1657. Determine if Two Strings Are Close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        frequency1 = calc_frequency(word1)
        frequency2 = calc_frequency(word2)
        keys1 = set(frequency1.keys())
        keys2 = set(frequency2.keys())
        values1 = list(frequency1.values())
        values2 = list(frequency2.values())
        values1.sort()
        values2.sort()
        return (keys1 == keys2) and (values1 == values2)


def calc_frequency(word: str):
    frequency = dict()
    for char in word:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

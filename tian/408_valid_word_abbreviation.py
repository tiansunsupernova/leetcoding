class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(abbr) and j < len(word):
            if abbr[i].isdigit():
                if abbr[i] == '0': return False
                cnt = 0
                while i < len(abbr) and abbr[i].isdigit():
                    cnt = cnt * 10 + int(abbr[i])
                    i += 1
                j += cnt
            else:
                if abbr[i] != word[j]: return False
                j += 1
                i += 1
        return j == len(word) and i == len(abbr)
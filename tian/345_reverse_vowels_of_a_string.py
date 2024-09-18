class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        s = list(s)
        vowels = set("aeiouAEIOU")
        while (i < j):
            while s[i] not in vowels and i < j:
                i += 1
            while s[j] not in vowels and i < j:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        s = "".join(s)
        return s

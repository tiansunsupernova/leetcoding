class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1 = {}
        d2 = {}

        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        for c, w in zip(pattern, words):
            if c in d1 and d1[c] != w:
                return False
            if w in d2 and d2[w] != c:
                return False
            d1[c] = w
            d2[w] = c
        return True

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        s1 = set()
        s2 = set()
        for c in word1:
            d1[c] += 1
            s1.add(c)
        for c in word2:
            d2[c] += 1
            s2.add(c)
        
        # not equal length
        if len(word1) != len(word2): return False
        # same characters
        if s1 != s2: return False
        # cnt are same if sorted
        return sorted(d1.values()) == sorted(d2.values())

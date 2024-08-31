class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        di = {}
        for c in s:
            if c not in di:
                di[c] = 0
            di[c] += 1
        for c in t:
            if c not in di:
                return False
            di[c] -= 1
        for v in di.values():
            if v != 0:
                return False
        return True
        

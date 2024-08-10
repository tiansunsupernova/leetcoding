class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        if len(s) != len(t): return False

        for i in range(len(s)):
            if (s[i] not in ds) and (t[i] not in dt):
                ds[s[i]] = t[i]
                dt[t[i]] = s[i]
            elif ds.get(s[i]) != t[i] or dt.get(t[i]) != s[i]:
                return False
        return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        di = defaultdict(int) # key = c, value = # left
        for c in t: di[c] -= 1
        cnt, j = 0, 0
        res = ""
        minL = float('inf')
        for i, c in enumerate(s):
            if c in di.keys():
                di[c] += 1
                if di[c] == 0:
                    cnt += 1     
            while cnt >= len(di.keys()):
                c = s[j]
                curL = i - j + 1
                if curL < minL:
                    res = s[j:i+1]
                    minL = curL
                if c in di.keys():
                    di[s[j]] -= 1
                    if di[s[j]] < 0: cnt -= 1
                j += 1
        return  res
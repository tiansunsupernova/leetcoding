class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        di = {}
                
        for c in order:
            di[c] = 0
        
        for ch in s:
            if ch not in di.keys():
                res.append(ch)
            else:
                di[ch] += 1
        
        for c in order:
            for _ in range(di[c]): res.append(c)
        
        return ''.join(res)
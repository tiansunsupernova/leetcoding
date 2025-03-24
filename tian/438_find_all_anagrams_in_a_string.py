class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        di = defaultdict(int)
        res = []
        k = len(p)
        
        for c in p:
            di[c] += 1

        cnt = len(di)
        
        for i, c in enumerate(s):
            if c in di:
                di[c] -= 1
                if di[c] == 0: cnt -= 1
            if i >= k:
                old_c = s[i - k]
                if old_c in di:
                    if di[old_c] == 0: cnt += 1
                    di[old_c] += 1
            if cnt == 0: res.append(i-k+1)
        
        return res
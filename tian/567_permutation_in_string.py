class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        di = defaultdict(int)
        k = len(s1)

        for c in s1:
            di[c] += 1
        
        cnt = len(di)

        for i, c in enumerate(s2):
            if c in di:
                di[c] -= 1
                if di[c] == 0: cnt -= 1
            if i >= k:
                old_c = s2[i - k]
                if old_c in di:
                    if di[old_c] == 0: cnt += 1
                    di[old_c] += 1
            if cnt == 0: return True
        
        return False
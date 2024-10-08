class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        cnt = 0
        for c in s:
            if c == '(': cnt += 1
            else: 
                if cnt >= 1: cnt -= 1
                else: res += 1
        
        return res + cnt
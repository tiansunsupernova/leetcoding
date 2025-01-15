class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        cnt = 0
        for i in range(k):
            if s[i] in vowels: cnt += 1
        res = cnt

        for i in range(k, len(s)):
            if s[i] in vowels: cnt += 1
            if s[i - k] in vowels: cnt -= 1
            res = max(res, cnt)
        
        return res

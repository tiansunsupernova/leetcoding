class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = 0
        max_l = 0
        for end, c in enumerate(s):
            if c not in d:
                d[c] = 0
            d[c] += 1
            while d[c] > 1:
                d[s[start]] -= 1
                start += 1
            max_l = max(max_l, end - start + 1)
        return max_l

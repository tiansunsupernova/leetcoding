class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = [0, 0]
        for i in range(n):
            dp[i][i] = True

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if s[i] == s[j] and (j + 1 >= i or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i - j  > res[1] - res[0]: res = [j, i]
        
        return s[res[0]:res[1] + 1]
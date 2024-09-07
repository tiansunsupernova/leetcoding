class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for word in wordDict:
                    l = len(word)
                    if s[i:i+l] == word: 
                        dp[i+l] = True
        return dp[n]
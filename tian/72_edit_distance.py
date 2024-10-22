class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        def recur(word1, word2, i, j):
            if i == 0: return j
            if j == 0: return i
            if dp[i][j] is not None: return dp[i][j]
            cnt = 0
            if word1[i - 1] == word2[j - 1]:
                cnt = recur(word1, word2, i - 1, j - 1)
            else:
                insert = recur(word1, word2, i, j - 1)
                delete = recur(word1, word2, i - 1, j)
                replace = recur(word1, word2, i - 1, j - 1)
                cnt = min(insert, delete, replace) + 1
            dp[i][j] = cnt
            return cnt   
        
        return recur(word1, word2, len(word1), len(word2))
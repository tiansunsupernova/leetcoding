class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        maxsqlen = 0

        for i in range(1, 1 + rows):
            for j in range(1, 1 + cols):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1]
                    ) + 1
                    maxsqlen = max(dp[i][j], maxsqlen)
        
        return maxsqlen * maxsqlen
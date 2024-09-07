class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            if dp[i] != float('inf') :
                for c in coins:
                    if i + c <= amount:
                        dp[i + c] = dp[i] + 1 if not dp[i + c] else min(dp[i] + 1, dp[i + c])
        return dp[amount] if dp[amount] != float('inf') else -1
                        
                     
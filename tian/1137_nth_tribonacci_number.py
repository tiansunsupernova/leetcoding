class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i):
            if i == 0: return 0
            if i == 1: return 1
            if i == 2: return 1
            return dfs(i-1) + dfs(i-2) + dfs(i-3)
        return dfs(n)
        
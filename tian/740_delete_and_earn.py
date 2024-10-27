class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        di = defaultdict(int) # k = num, v = points
        lo, hi = 10000, 1
        for x in nums:
            di[x] += x
            lo = min(lo, x)
            hi = max(hi, x)
        
        @lru_cache(None)
        def dfs(i):
            if i < lo: return 0
            if i not in di.keys():
                return max(dfs(i - 1), dfs(i - 2))
            return max(dfs(i - 2), dfs(i - 3)) + di[i]
        return max(dfs(hi),dfs(hi - 1))
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        
        @lru_cache(None)
        def dfs(lo, hi, i):
            if i >= m: return 0 
            start_product = multipliers[i] * nums[lo] + dfs(lo + 1, hi, i + 1)
            end_product = multipliers[i] * nums[hi] + dfs(lo, hi - 1, i + 1)
            return max(start_product, end_product)
        
        return dfs(0, n - 1, 0)
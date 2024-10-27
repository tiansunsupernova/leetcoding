class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(i, subSum) -> bool:
            if subSum == 0: return True
            if i == 0 or subSum < 0: return False
            res = (dfs(i - 1, subSum - nums[i]) or
            dfs(i - 1, subSum))
            return res

        s = sum(nums)
        if s % 2 == 1: return False
        return dfs(len(nums) - 1, s // 2)
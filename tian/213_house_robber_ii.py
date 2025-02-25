class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        return max(self.dp(tuple(nums), n - 2, True), self.dp(tuple(nums), n - 1, False))
    
    @lru_cache
    def dp(self, nums, i, robZero):
        if i == 0:
            return nums[0] if robZero else 0
        if i == 1:
            return nums[0] if robZero else nums[1]
        return max(nums[i] + self.dp(nums, i - 2, robZero), self.dp(nums, i - 1, robZero))
        
        
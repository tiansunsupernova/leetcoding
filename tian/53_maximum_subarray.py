class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]
        cur = nums[0]
        for i, num in enumerate(nums[1:]):
            if cur < 0:
                cur = 0
            cur += num
            max_total = max(cur, max_total)
        return max_total
            
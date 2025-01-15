class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt, fast, slow = 0, 0, 0
        res = 0
        for fast in range(len(nums)):
            if nums[fast] == 0: cnt += 1
            while cnt > 1:
                if nums[slow] == 0: cnt -= 1
                slow += 1
            res = max(res, fast - slow)
        return res
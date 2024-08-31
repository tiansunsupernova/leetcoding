class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, start = 0, 0
        minlen = None
        for end, v in enumerate(nums):
            total += v
            while (total >= target):
                minlen = min(minlen, end - start + 1) if minlen else end - start + 1
                total -= nums[start]
                start += 1
        return minlen if minlen else 0

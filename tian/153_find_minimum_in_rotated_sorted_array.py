class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
        while (lo <= hi):
            mi = (lo + hi) >> 1
            if nums[mi] < nums[mi - 1]:
                return nums[mi]
            elif nums[mi] >= nums[0]:
                lo = mi + 1
            else:
                hi = mi - 1
        return -1

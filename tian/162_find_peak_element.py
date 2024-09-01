class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mi = (lo + hi) >> 1
            leftSmall = mi == 0 or nums[mi] > nums[mi - 1]
            rightSmall = mi == len(nums) - 1 or nums[mi] > nums[mi + 1]
            if leftSmall and rightSmall:
                return mi
            elif leftSmall:
                lo = mi + 1
            else:
                hi = mi - 1
        return lo
            
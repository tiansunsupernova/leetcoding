class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mi = (lo + hi) >> 1
            if nums[mi] == target:
                return mi
            if nums[mi] < nums[lo]:
                if target > nums[mi] and target <= nums[hi]:
                    lo = mi + 1
                else:
                    hi = mi - 1
            else:
                if target >= nums[lo] and target < nums[mi]:
                    hi = mi - 1
                else:
                    lo = mi + 1
        return -1
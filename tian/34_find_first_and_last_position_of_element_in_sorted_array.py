class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        first, second = -1, -1
        while lo <= hi:
            mi = (lo + hi) >> 1
            if nums[mi] == target and (mi == 0 or nums[mi] != nums[mi - 1]):
                first = mi
                break
            elif nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi - 1
        lo, hi = 0, len(nums) - 1         
        while lo <= hi:
            mi = (lo + hi) >> 1
            if nums[mi] == target and (mi == len(nums) - 1 or nums[mi] != nums[mi + 1]):
                second = mi
                break
            elif nums[mi] > target:
                hi = mi - 1
            else:
                lo = mi + 1
        return [first, second]
            
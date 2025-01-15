class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        csum = 0
        s = sum(nums)
        for i, v in enumerate(nums):
            # left sum = csum
            # right sum = s - csum - v
            if s - csum - v == csum: return i
            csum += v
        return - 1
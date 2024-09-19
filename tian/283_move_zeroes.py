class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for v in nums:
            if v != 0:
                nums[j] = v
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
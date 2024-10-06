class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        while right - 1 >= 0 and nums[right] <= nums[right - 1]:
            right -= 1
        # num[right - 1] is the first item that's smaller than nums[right]
        if right >= 1:
            k = len(nums) - 1
            while nums[k] <= nums[right - 1]:
                k -= 1
            # k is the right most index with nums[k] > nums[right - 1]
            self.swap(nums, k, right - 1)
        self.reverse(nums, right)
 

    def reverse(self, nums, start):
        end = len(nums) - 1
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
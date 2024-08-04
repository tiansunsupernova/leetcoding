class Solution:
# 1 2 3 4
# 1 1 2 6
# 24  12  4 1

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        li = [0] * n
        li[0] = 1 
        for i in range(1, n):
            li[i] = li[i - 1] * nums[i - 1]

        prod = 1
        for i in reversed(range(n)):
            li[i] *= prod
            prod *= nums[i]
        return li


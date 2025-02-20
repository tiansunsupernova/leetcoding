class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [False] * (n)
        for x in nums:
            if x <= n and x > 0: 
                arr[x - 1] = True
        for i in range(n):
            if not arr[i]: return i + 1
        return n + 1
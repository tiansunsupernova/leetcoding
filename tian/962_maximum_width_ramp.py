class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [i for i in range(n)]
        
        arr.sort(key = lambda i : (nums[i], i))

        min_x = float('inf')
        res = 0

        for x in arr:
            if x >= min_x:
                res = max(res, x - min_x)
            else:
                min_x = x
        
        return res
        
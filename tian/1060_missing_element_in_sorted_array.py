class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # if len(nums) == 1:
        #     return nums[0] + k
        # for i in range(1, len(nums)):
        #     if nums[i] > num[i - 1] + 1:
        #         k -= nums[i] - 1 - num[i - 1]
        #         if k <= 0: return nums[i] - 1 + k 
        def count(mi):
            return (nums[mi] - nums[0]) - (mi - 0)
        
        def bsearch():
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mi = (lo + hi) // 2
                if count(mi) < k and (mi == len(nums) - 1 or count(mi + 1) >= k):
                    return mi
                elif count(mi) < k:
                    lo = mi + 1
                else:
                    hi = mi - 1
            return lo
        
        i = bsearch()
        return nums[i] +  (k - count(i))
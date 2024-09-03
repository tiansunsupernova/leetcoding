class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        di = {} # k = val of num, v = cumulative sum of key
        # csum(nums[j]) - csum(nums[j] + k), csum(nums[j]) - csum(nums[j] + k)
        if not nums: return 0
        res, csum = float('-inf'), 0
        for x in nums:
            cur_csum = csum + x
            if (x + k) in di:
                old_csum = di[x + k]
                res = max(res, cur_csum - old_csum)
            if (x - k) in di:
                old_csum = di[x - k]
                res = max(res, cur_csum - old_csum)
            di[x] = min(di[x], csum) if x in di else csum
            csum = cur_csum
        return 0 if res == float('-inf') else res


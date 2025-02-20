class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        di = {} # k = sum % k, v = last index
        csum = 0
        di[0] = -1
        for i in range(len(nums)):
            csum = (csum + nums[i]) % k
            if csum in di:
                if i - di[csum] >= 2: return True
            else:
                di[csum] = i
        return False

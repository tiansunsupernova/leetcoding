class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCnt, j = 0, 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0: zeroCnt += 1
            if zeroCnt > k:
                while zeroCnt > k and j < i:
                    if nums[j] == 0: zeroCnt -= 1
                    j += 1
            if zeroCnt <= k: res = max(res, i - j + 1)
        return res

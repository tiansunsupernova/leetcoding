class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # x: number of 1 - number of 0
        di = {} # k = x, v = index
        x = 0
        res = 0
        di[0] = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                x -= 1
            else:
                x += 1
            if x not in di:
                di[x] = i
            if x in di:
                res = max(res, i - di[x])
        return res



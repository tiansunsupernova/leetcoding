class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i, v1 in enumerate(nums):
            v2 = target - v1
            if v2 in di:
                return [di[v2], i]
            else:
                di[v1] = i
        return [0, 0]

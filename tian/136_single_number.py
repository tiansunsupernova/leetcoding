class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = nums[0]
        for x in nums[1:]:
            num ^= x
        return num 

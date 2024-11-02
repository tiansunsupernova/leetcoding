class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        last = lower - 1 # last missing
        for num in nums:
            if num <= last + 1:
                last = num
                continue
            if last >= upper: 
                last = num
                continue
            res.append([last + 1, num - 1])
            last = num
        if last < upper: res.append([last + 1, upper])
        return res

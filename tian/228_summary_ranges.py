class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start, end, res = nums[0], nums[0], []
        for i, v in enumerate(nums):
            if i > 0:
                if v == end + 1:
                    end = v
                else:
                    if start == end:
                        res.append(str(end))
                    else:
                        res.append(str(start) + "->" + str(end))
                    start = v
                    end = v
        if start == end:
            res.append(str(end))
        else:
            res.append(str(start) + "->" + str(end))
        return res
            


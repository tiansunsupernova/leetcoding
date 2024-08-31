class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def btrack(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for n in nums:
                if n not in cur:
                    cur.append(n)
                    btrack(cur)
                    cur.pop()
        
        res = []
        btrack([])
        return res
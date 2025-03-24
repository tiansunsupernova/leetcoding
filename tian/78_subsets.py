class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def btrack(cur, i):
            if i == len(nums):
                res.append(list(cur))
                return
            # use item i
            cur.append(nums[i])
            btrack(cur, i + 1)
            cur.pop()

            # not use item i
            btrack(cur, i + 1)
            
        btrack([], 0)
        return res
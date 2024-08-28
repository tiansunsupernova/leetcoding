class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def btrack(cur, remain, idx):
            if remain == 0:
                res.append(cur[:])
                return
            if remain < 0:
                return
            for i in range(idx, len(candidates)):
                num = candidates[i]
                cur.append(num)
                btrack(cur, remain - num, i)
                cur.pop()

        res = []
        btrack([], target, 0)
        return res
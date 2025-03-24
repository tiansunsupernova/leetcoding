class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def btrack(cur, s, start):
            if s == target:
                res.append(list(cur))
                return
            elif s > target:
                return
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    if s + candidates[i] > target:
                        break
                    cur.append(candidates[i])
                    btrack(cur, s + candidates[i], i + 1)
                    cur.pop()
                    
        res = []
        candidates.sort()
        print(candidates)
        btrack([], 0, 0)
        return res


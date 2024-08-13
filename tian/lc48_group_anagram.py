class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {} # key = sorted s, value = s
        res = []
        for st in strs:
            sorted_st = "".join(sorted(st))
            if sorted_st not in di:
                di[sorted_st] = []
            di[sorted_st].append(st)
        for v in di.values():
            res.append(v)
        return res

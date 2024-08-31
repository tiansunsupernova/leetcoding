class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for x in intervals:
            if not res or res[-1][1] < x[0]:
                res.append(x)
            else:
                res[-1][1] = max(x[1],res[-1][1])
        return res
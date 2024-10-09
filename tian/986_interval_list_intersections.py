class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0 , 0
        res = []

        while i < len(firstList) and j < len(secondList):
            a = firstList[i]
            b = secondList[j]

            lo = max(a[0], b[0])
            hi = min(a[1], b[1])

            if lo <= hi:
                res.append([lo, hi])

            if a[1] < b[1]:
                i += 1
            else:
                j += 1
        
        return res


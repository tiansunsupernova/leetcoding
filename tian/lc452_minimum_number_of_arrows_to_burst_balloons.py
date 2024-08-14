class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x: x[1])
        
        res = 1
        old_j = points[0][1]
        for x_i, x_j in points:
            if old_j < x_i:
                res += 1
                old_j = x_j
        return res


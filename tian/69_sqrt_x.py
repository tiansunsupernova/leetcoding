class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x // 2
        while lo <= hi:
            mi = (lo + hi) >> 1
            if mi * mi <= x and (mi+1) * (mi+1) > x:
                return mi
            elif mi * mi > x:
                hi = mi - 1
            else:
                lo = mi + 1
        return 1
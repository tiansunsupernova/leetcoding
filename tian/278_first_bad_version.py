# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mi = (lo + hi) // 2
            if  (mi == 1 or not isBadVersion(mi - 1)) and isBadVersion(mi):
                return mi
            elif (mi == 1 or not isBadVersion(mi - 1)):
                lo = mi + 1
            else:
                hi = mi - 1
        return -1
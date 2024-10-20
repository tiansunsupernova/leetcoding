class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search, k from 1 to max(pile)
        lo, hi = 1, max(piles)

        while lo <= hi:
            k = (lo + hi) >> 1
            if self.counter(piles, k) <= h and (k == 1 or self.counter(piles, k - 1) > h):
                return k
            elif k > 1 and self.counter(piles, k - 1) <= h:
                hi = k - 1
            else:
                lo = k + 1
        return lo

    def counter(self, piles, k):
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        return hours
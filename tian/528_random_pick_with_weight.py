class Solution:

    def __init__(self, w: List[int]):
        self.li = []
        self.total = 0
        self.w = w
        for x in w:
            self.total += x
            self.li.append(self.total)

    def pickIndex(self) -> int:
        target = math.ceil(self.total * random.random())
        lo, hi = 0, len(self.li) - 1
        while lo <= hi:
            mi = (lo + hi) >> 1
            if target == self.li[mi]:
                return mi
            elif target > self.li[mi]:
                lo = mi + 1
            else:
                hi = mi - 1
        return lo
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
class Solution:
    # def __init__(self):
    #     self.events = None

    # def maxValue(self, events: List[List[int]], k: int) -> int:
    #     self.events = sorted(events, key = lambda x : x[1])
    #     lastEnd = self.events[-1][1]
    #     return self.dp(lastEnd + 1, k)

    # @lru_cache(None)
    # def dp(self, cur, cnt):
    #     if cnt <= 0: return 0
    #     maxVal = 0
    #     for e in self.events:
    #         if e[1] >= cur:
    #             break
    #         newCur = e[0]
    #         value = e[2] + self.dp(newCur, cnt - 1)
    #         maxVal = max(maxVal, value)
    #     return maxVal

    def __init__(self):
        self.events = None

    def maxValue(self, events: List[List[int]], k: int) -> int:
        self.events = sorted(events, key = lambda x : (x[1], x[0]))
        last_i = len(self.events) - 1
        return self.dp(last_i, k)

    @lru_cache(None)
    def dp(self, i, cnt):
        if cnt <= 0 or i < 0: return 0
        next_i = self.find(i)
        return max(self.dp(i - 1, cnt), 
        self.events[i][2] + self.dp(next_i, cnt - 1))
    
    @lru_cache(None)
    def find(self, i):
        nextStart = self.events[i][0]
        lo, hi = 0, i - 1
        while lo <= hi:
            mi = (lo + hi) >> 1
            if self.events[mi][1] < nextStart and (mi == i - 1 or self.events[mi + 1][1] >= nextStart):
                return mi
            elif self.events[mi][1] < nextStart:
                lo = mi + 1
            else:
                hi = mi - 1
        return -1


    

# dp(5, 2)
# e = [1,2,4] [2,3,1] [3, 4, 3]
# newCur = 1 2 3
# val = 4 + 0 | 1 + 0 | 3 + 4

# dp(3, 1)
# e = [1,2, 4]
# newCur = 1
# val = 4 + 0

# dp()
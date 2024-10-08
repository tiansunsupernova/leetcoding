class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        buckets = [False] * (24 * 60)
        for timePoint in timePoints:
            time = timePoint.split(':')
            minutes = int(time[0]) * 60 + int(time[1])
            if buckets[minutes]: return 0
            buckets[minutes] = True
        
        li = []
        for i,v in enumerate(buckets):
            if v: li.append(i)

        res = float('inf')
        for i in range(len(li)):
            res = min(res, (li[i] - li[(i - 1) % len(li)]) % (24 * 60))
        return res
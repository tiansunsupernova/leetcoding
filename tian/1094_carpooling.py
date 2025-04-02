class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = []
        for x in trips:
            timestamp.append((x[1], x[0]))
            timestamp.append((x[2], -x[0]))
        
        timestamp.sort()

        cur = 0
        for time, diff in timestamp:
            cur += diff
            if cur > capacity: return False
        return True

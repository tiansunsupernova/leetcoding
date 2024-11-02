class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        h = []
        cnt = 0

        for x in intervals:
            heapq.heappush(h, (x[1], x))
            while h[0][0] <= x[0]:
                heapq.heappop(h)
            cnt = max(cnt, len(h))

        return cnt
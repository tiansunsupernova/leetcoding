class Solution:
    def reorganizeString(self, s: str) -> str:
        h = []
        di = defaultdict(int)
        
        for c in s: di[c] += 1
        for c in di.keys(): heapq.heappush(h, (-di[c], di[c], c))

        res = []

        while h:
            _, cnt, c = heapq.heappop(h)
            if not res or c != res[-1]:
                res.append(c)
                if cnt - 1 > 0: heapq.heappush(h, (1 - cnt, cnt - 1, c))
            else:
                if not h: return ""
                _, cnt2, c2 = heapq.heappop(h)
                res.append(c2)
                if cnt2 - 1 > 0: heapq.heappush(h, (1- cnt2, cnt2 - 1, c2))
                heapq.heappush(h, (-cnt, cnt, c))
        
        return "".join(res)
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        h_left = costs[:candidates] 
        h_right = costs[max(candidates, len(costs) - candidates):]
        heapify(h_left)
        heapify(h_right)
        res = 0
        l = len(h_left)
        r = len(costs) - 1 - len(h_right)

        for i in range(k):
            if not h_right or h_left and h_left[0] <= h_right[0]:
                res += heapq.heappop(h_left)
                if l <= r:
                    heapq.heappush(h_left, costs[l])
                    l += 1
            else:
                res += heapq.heappop(h_right)
                if l <= r:
                    heapq.heappush(h_right, costs[r])
                    r -= 1
            
        return res
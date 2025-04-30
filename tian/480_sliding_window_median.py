class Solution:
    def findMedian(self, lo, hi, k):
        if k % 2 == 1:
            return -lo[0]
        else:
            return (-lo[0] + hi[0]) / 2

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo = [] # max heap
        hi = [] # min heap
        di = defaultdict(int)
        res = []

        # preloading k items
        for i in range(k):
            heapq.heappush(lo, -nums[i])

        for _ in range(k//2):
            x = -heapq.heappop(lo)
            heapq.heappush(hi, x)

        median = self.findMedian(lo, hi, k)
        res.append(median)

        for i in range(k, len(nums)):
            prev = nums[i - k]
            di[prev] += 1

            balance = -1 if prev <= median else 1

            if nums[i] <= median: 
                balance += 1
                heapq.heappush(lo, -nums[i])
            else:
                balance -= 1
                heapq.heappush(hi, nums[i])
            
            if balance < 0:
                heapq.heappush(lo, -heapq.heappop(hi))
            elif balance > 0:
                heapq.heappush(hi, -heapq.heappop(lo))

            while lo and di[-lo[0]] > 0:
                di[-lo[0]] -= 1
                heapq.heappop(lo)

            while hi and di[hi[0]] > 0:
                di[hi[0]] -= 1
                heapq.heappop(hi)

            median = self.findMedian(lo, hi, k)
            res.append(median)
        
        return res

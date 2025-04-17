class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        l = len(nums)
        arr = sorted((nums[i],i) for i in range(l))
        l_heap, r_heap = [], []
        min_diff = float('inf')

        for val, idx in arr:
            heapq.heappush(l_heap, (idx, val))
            heapq.heappush(r_heap, (-idx, val))
            while l_heap and idx - l_heap[0][0] >= x:
                min_diff = min(min_diff, val - heapq.heappop(l_heap)[1])
            while r_heap and -r_heap[0][0] - idx >= x:
                min_diff = min(min_diff, val - heapq.heappop(r_heap)[1])

        return min_diff
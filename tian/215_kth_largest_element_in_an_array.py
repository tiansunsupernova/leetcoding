# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = []
#         for num in nums:
#             heapq.heappush(heap, num)
#             if len(heap) > k:
#                 heapq.heappop(heap)
#         return heap[0]
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left, mid, right = [], [], []
        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else: 
                mid.append(num)
        
        if k <= len(left): return self.findKthLargest(left, k)
        if len(left) + len(mid) < k: return self.findKthLargest(right, k - len(left) - len(mid))
        return pivot
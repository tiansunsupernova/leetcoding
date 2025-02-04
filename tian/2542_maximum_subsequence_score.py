class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        arr = [[nums1[i], nums2[i]] for i in range(n)]
        arr.sort(key = lambda x: -x[1])

        h = []
        res = 0
        s = 0
    
        for i in range(k):
            s += arr[i][0]
            heapq.heappush(h, arr[i][0])
    
        res = s * arr[k-1][1]

        for i in range(k, n):
            s = s + arr[i][0] - heapq.heappop(h)
            heapq.heappush(h, arr[i][0])
            print(s, arr[i])
            res = max(res, arr[i][1] * s)

        return res
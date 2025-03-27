class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix) 
        h = []

        for i in range(n):
            heapq.heappush(h, (matrix[i][0], i, 0))

        val = -1

        while h and k > 0:
            val, i, j = heapq.heappop(h)
            if j + 1 < n:
                heapq.heappush(h, (matrix[i][j + 1], i, j + 1))
            k -= 1
        return val

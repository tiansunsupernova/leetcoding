class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = [[False] * n for i in range(n)]
        largest = 0
        h = []
        heapq.heappush(h, (grid[0][0], 0, 0))
        while h:
            cur_val, cur_i, cur_j = heapq.heappop(h)
            largest = max(cur_val, largest)
            if cur_i == n-1 and cur_j == n-1:
                return largest
            seen[cur_i][cur_j] = True
            li = self.neighbors(grid, cur_i, cur_j, n)
            for i in range(len(li)):
                next_val, next_i, next_j = li[i]
                if seen[next_i][next_j]:
                    continue
                heapq.heappush(h, (next_val, next_i, next_j))
        return -1
    
    def neighbors(self, grid, i, j, n) -> List[int]:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        res = []
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if x < 0 or y < 0 or x >=n or y >= n: 
                continue
            else:
                res.append((grid[x][y], x, y))
        return res
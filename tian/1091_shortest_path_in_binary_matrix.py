class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        seen = set((0,0))
        l = len(grid)
        if grid[0][0] == 1:
            return -1
        
        dx = [0, 0, 1, -1, 1, -1, 1, -1]
        dy = [1, -1, 0, 0, 1, -1, -1, 1]

        q = deque([(0, 0)])
        cnt = 1
        while q:
            items = len(q)
            for _ in range(items):
                i, j = q.popleft()
                if i == l - 1 and j == l - 1: return cnt
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if x >= 0 and x < l and y >= 0 and y < l and grid[x][y] == 0 and (x, y) not in seen:
                        q.append((x, y))
                        seen.add((x, y))
            cnt += 1
        return -1

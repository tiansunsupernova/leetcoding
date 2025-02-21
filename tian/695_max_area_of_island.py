class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, self.visit(grid, i, j))
        return res
    
    def visit(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        cnt = 1
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        grid[i][j] = 0
        for k in range(4):
            cnt += self.visit(grid, i + dx[k], j + dy[k])
        return cnt

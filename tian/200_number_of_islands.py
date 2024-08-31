class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.traverse(grid, i, j) 
                    cnt += 1
        return cnt
    
    def traverse(self, grid, i, j) -> None:
        if (
            i < 0
            or j < 0
            or i >= len(grid)
            or j >= len(grid[0])
            or grid[i][j] != "1"
        ): return

        grid[i][j] = "0"
        self.traverse(grid, i + 1, j)
        self.traverse(grid, i - 1, j)
        self.traverse(grid, i, j + 1)
        self.traverse(grid, i, j - 1)
        

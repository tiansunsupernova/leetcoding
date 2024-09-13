class Solution:
    def __init__(self):
        self.isBorder = False
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    self.isBorder = False
                    self.traverse(grid, i, j)
                    if not self.isBorder:
                        cnt += 1
        return cnt
    
    def traverse(self, grid: List[List[int]], i: int, j :int):
        rows, cols = len(grid), len(grid[0])
        
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 1:
            return

        if i == 0 or j == 0 or i == rows - 1 or j == cols -1:
            self.isBorder = True
        
        grid[i][j] = 1
        self.traverse(grid, i + 1, j)
        self.traverse(grid, i - 1, j)
        self.traverse(grid, i, j + 1)
        self.traverse(grid, i, j - 1)


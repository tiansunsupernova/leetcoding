class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                elif i == 0: 
                    grid[i][j] = grid[i][j] + grid[i][j - 1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i - 1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i][j - 1], grid[i - 1][j])
        return grid[len(grid) - 1][len(grid[0]) - 1]
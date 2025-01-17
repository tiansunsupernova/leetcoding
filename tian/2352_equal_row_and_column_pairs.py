class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cnt = 0

        dict_row = defaultdict(int)
        for i in range(n):
            row_li = tuple(grid[i]) 
            dict_row[row_li] += 1
        
        for j in range(n):
            col_li = tuple([row[j] for row in grid])
            if col_li in dict_row:
                cnt += dict_row[col_li]
        return cnt
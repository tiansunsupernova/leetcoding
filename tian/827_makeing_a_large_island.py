class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def traverse(i, j, key):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return
            grid[i][j] = key
            di[key] += 1

            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            for z in range(4):
                x = i + dx[z]
                y = j + dy[z]
                traverse(x, y, key)
        
        key = 0
        di = defaultdict(int) # k = key, v = cnt
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    key -= 1
                    traverse(i, j, key)

        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0: 
                    res = max(res, di[grid[i][j]])
                else:
                    s = set()
                    dx = [0, 0, 1, -1]
                    dy = [1, -1, 0, 0]
                    for z in range(4):
                        x = i + dx[z]
                        y = j + dy[z]
                        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0: continue
                        s.add(grid[x][y])
                    arr = []
                    for k in s:
                        arr.append(di[k])
                    arr.sort(key = lambda x:-x)
                    res = max(res, sum(arr) + 1)

        return res

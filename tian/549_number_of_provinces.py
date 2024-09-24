class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in range(n)]
        rank = [1] * n


        def find(x):
            # union find with path compression
            if root[x] == x:
                return x
            root[x] = find(root[x]) 
            return root[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1


        res = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and find(i) != find(j):
                    union(i, j)
                    res -= 1
        return res
    
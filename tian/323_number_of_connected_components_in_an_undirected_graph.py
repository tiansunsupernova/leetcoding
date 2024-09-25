class Solution:
    def __init__(self):
        self.root = None
        self.rank = None
        self.cnt = 0

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.cnt = n
        self.rank = [1] * n
        self.root = [i for i in range(n)]

        for e in edges:
            self.union(e[0], e[1])
        
        return self.cnt
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
            self.cnt -= 1
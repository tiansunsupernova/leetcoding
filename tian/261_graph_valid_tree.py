class Solution:
    def __init__(self):
        self.rank = None
        self.root = None
        self.hasCycle = False
        self.cnt = None

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.cnt = n

        for e in edges:
            self.union(e[0], e[1])
            if self.hasCycle: return False
        
        return self.cnt == 1
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.cnt -= 1
        else:
            self.hasCycle = True

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
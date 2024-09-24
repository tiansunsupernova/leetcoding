class Solution:
    def __init__(self):
        self.rank = None
        self.root = None
        self.cnt = None

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        self.rank = [1] * n
        self.root = [i for i in range(n)]
        self.cnt = n

        logs.sort(key=lambda x: x[0])

        for log in logs:
            self.union(log[1], log[2])
            if self.cnt == 1:
                return log[0]

        return -1
    
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

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]


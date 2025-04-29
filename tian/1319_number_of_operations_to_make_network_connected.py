class Solution:
    def __init__(self):
        self.root = None
        self.cnt = 0

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootX] = self.root[rootY]
            self.cnt += 1            

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        self.root = [i for i in range(n)]

        for e in connections:
            self.union(e[0], e[1])

        # n - 1 - effective edges = ans
        # -> ans = effective edges + 1 - n

        return n - 1 - self.cnt







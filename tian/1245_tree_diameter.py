class Solution: 
    def __init__(self):
        self.res = 0

    def dfs(self, arr, node, prev):
        # 1. update max with current longest 1st + 2nd child pass
        # 2. return the longest 1st
        children = arr[node]

        first = -1
        second = -1

        for child in children:
            if child == prev:
                continue
            v = self.dfs(arr, child, node)
            
            if v >= first:
                second = first
                first = v
            elif v >= second:
                second = v
        
        if first < 0: 
            return 0
        elif second < 0: 
            self.res = max(self.res, first + 1)
            return first + 1      
        else:
            self.res = max(self.res, first + second + 2)
            return first + 1 

    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        arr = [[] for _ in range(n)]
        
        # build adjacency list
        for e in edges:
            arr[e[0]].append(e[1])
            arr[e[1]].append(e[0])
        
        # always start from 0
        self.dfs(arr, 0, -1)
        
        return self.res
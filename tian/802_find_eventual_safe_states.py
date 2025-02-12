class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outDegree = [0] * n

        res = [False] * n
        
        q = deque()

        inNodes = [[] for _ in range(n)]

        for i in range(n):
            outDegree[i] = len(graph[i])
            if outDegree[i] == 0:
                q.append(i)
            for x in graph[i]:
                inNodes[x].append(i)

        while q:
            cur = q.popleft()
            res[cur] = True
            for node in inNodes[cur]:
                outDegree[node] -= 1
                if outDegree[node] == 0:
                    q.append(node)
        
        return [i for i in range(n) if res[i]]
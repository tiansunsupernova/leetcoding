class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        e = [set() for _ in range(n)]
        
        for start,end in edges:
            e[start].add(end)
            e[end].add(start)
        
        q = []

        for i in range(n):
            if len(e[i]) <= 1: q.append(i)
        
        cnt = n
        while cnt > 2:
            cnt -= len(q)
            new_q = []
            while q:
                cur = q.pop()
                next = e[cur].pop()
                e[next].remove(cur)
                if len(e[next]) == 1:
                    new_q.append(next)
            q = new_q    
        return q
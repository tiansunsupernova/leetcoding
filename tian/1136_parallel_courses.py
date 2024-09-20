class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        #1 calculate inDegree of all courses, put inDegree == 0 to q
        inDegree = [0] * (n + 1)
        e = [[] for _ in range(n + 1)]
        for start,end in relations:
            e[start].append(end)
            inDegree[end] += 1
        q = deque()
        for i,v in enumerate(inDegree):
            if i!= 0 and v == 0:
                q.append(i)
        took, cnt = 0, 0
        #2 while q:
        #.   loop through inDegree = 0 nodes,
        #.   1) get curclass
        #.   2) for each outgoing class of curclass: 
                    # inDegree[curclass] --
                    # if inDegree[curclass] == 0: q.add(curclass)
        #     cnt += 1
        while q:
            l = len(q)
            for i in range(l):
                cur = q.popleft()
                for new in e[cur]:
                    inDegree[new] -= 1
                    if inDegree[new] == 0:
                        q.append(new)
                took += 1
            cnt += 1
        #  return cnt (if still course in graph, return -1)
        return cnt if took == n else -1
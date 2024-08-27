class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        inDegree = [0] * numCourses
        e = [[] for _ in range(numCourses)]
        cnt = 0

        for p in prerequisites:
            e[p[1]].append(p[0])
            inDegree[p[0]] += 1

        q = deque() # zero in-degrees
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            for nextCourse in e[course]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    q.append(nextCourse)
            cnt += 1
        
        return cnt == numCourses

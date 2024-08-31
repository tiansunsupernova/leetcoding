class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        e = [[] for _ in range(numCourses)]
        res = []

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
            res.append(course)
        
        return res if len(res) == numCourses else []

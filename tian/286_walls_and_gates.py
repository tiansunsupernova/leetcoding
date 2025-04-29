class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #1. find all gates
        INF = 2147483647
        q = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    #2. put them into Q
                    q.append((i, j))

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        #3. traverse BFS
        step = 0
        while q:
            l = len(q)
            step += 1
            for i in range(l):
                x, y = q.popleft()
                for k in range(4):
                    newx = x + dx[k]
                    newy = y + dy[k]
                    if newx >= 0 and newy >= 0 and newx < len(rooms) and newy < len(rooms[0]) and rooms[newx][newy] == INF:
                        q.append((newx, newy))
                        rooms[newx][newy] = step
            
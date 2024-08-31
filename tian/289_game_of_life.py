class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = [0,0,1,-1,-1,-1,1,1]
        dy = [1,-1,0,0,-1,1,-1,1]

        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                cnt = 0
                for k in range(8):
                    di = i + dx[k]
                    dj = j + dy[k]
                    if di >= 0 and di < rows and dj >= 0 and dj < cols and board[di][dj] > 0:
                        cnt += 1
                if board[i][j] == 1:                    
                    if cnt < 2 or cnt > 3:
                        board[i][j] = 2 # cur live, next die
                    if cnt >= 2 and cnt <= 3:
                        board[i][j] = 1 # cur live, next live
                else:
                    if cnt == 3:
                        board[i][j] = -1 # cur die, next live

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1 or board[i][j] == -1:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
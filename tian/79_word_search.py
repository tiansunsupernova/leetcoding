class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def btrack(x, y, idx):
            if (idx == len(word)):
                return True
            if (x < 0 
            or y < 0
            or x >= len(board)
            or y >= len(board[0])
            or board[x][y] != word[idx]
            ): return False
            
            board[x][y] = "#"
            found = (btrack(x + 1, y, idx + 1) or
                     btrack(x, y + 1, idx + 1) or
                     btrack(x - 1, y, idx + 1) or
                     btrack(x, y - 1, idx + 1))
            board[x][y] = word[idx]
            return found
        
        
        if not board: return False
        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if btrack(i, j, 0): return True
        return False

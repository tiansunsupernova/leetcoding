class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (
                    i == 0
                    or j == 0
                    or i == len(board) - 1
                    or j == len(board[0]) - 1
                    and board[i][j] == "O"
                ): self.traverse(board, i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O": board[i][j] = "X"
                if board[i][j] == "P": board[i][j] = "O"

    def traverse(self, board: List[List[str]], i: int, j: int) -> None:
        if (
            i < 0
            or j < 0
            or i >= len(board)
            or j >= len(board[0])
            or board[i][j] != "O"
        ): return
        board[i][j] = "P"
        self.traverse(board, i+1, j)
        self.traverse(board, i-1, j)
        self.traverse(board, i, j+1)
        self.traverse(board, i, j-1)
        
        
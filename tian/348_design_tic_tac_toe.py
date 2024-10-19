class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.p1_rows = [0] * n
        self.p2_rows = [0] * n
        self.p1_cols = [0] * n
        self.p2_cols = [0] * n
        self.p1_cross1 = 0
        self.p2_cross1 = 0
        self.p1_cross2 = 0
        self.p2_cross2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.p1_rows[row] += 1
            self.p1_cols[col] += 1
            if row == col: self.p1_cross1 += 1
            if row + col == self.n - 1: self.p1_cross2 += 1

            if (self.p1_rows[row] == self.n or
            self.p1_cols[col] == self.n or
            self.p1_cross1 == self.n or
            self.p1_cross2 == self.n): return 1
        else:
            self.p2_rows[row] += 1
            self.p2_cols[col] += 1
            if row == col: self.p2_cross1 += 1
            if row + col == self.n - 1: self.p2_cross2 += 1

            if (self.p2_rows[row] == self.n or
            self.p2_cols[col] == self.n or
            self.p2_cross1 == self.n or
            self.p2_cross2 == self.n): return 2
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        r_zero = [False] * rows
        c_zero = [False] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    r_zero[r] = True
                    c_zero[c] = True
        
        for r in range(rows):
            for c in range(cols):
                if r_zero[r] or c_zero[c]:
                    matrix[r][c] = 0
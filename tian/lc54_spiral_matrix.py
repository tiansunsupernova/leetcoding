class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c = 0, -1
        rows = len(matrix)
        cols = len(matrix[0])
        direction = 1
        
        res = []

        while rows > 0 and cols > 0:
            
            for _ in range(cols):
                c += direction
                res.append(matrix[r][c])

            rows -= 1

            for _ in range(rows):
                r += direction
                res.append(matrix[r][c])
            cols -= 1

            direction *= -1
        return res

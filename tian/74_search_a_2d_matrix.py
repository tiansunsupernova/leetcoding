class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        end = rows * cols - 1

        while start <= end:
            mi = (start + end) >> 1
            cur = matrix[mi // cols][mi % cols]
            if cur == target:
                return True
            elif cur > target:
                end = mi - 1
            else:
                start = mi + 1
        return False


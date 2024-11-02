class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        di = defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                key = i - j
                if key in di:
                    if di[key] != matrix[i][j]: return False
                else:
                    di[key] = matrix[i][j]
        return True
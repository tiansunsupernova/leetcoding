class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        res = [[] for _ in range(n + m - 1)]
        for i in range(n):
            for j in range(m):
                res[i + j].append(mat[i][j])
        arr = []
        for i in range(len(res)):
            if i % 2 == 0:
                res[i].reverse()
            arr.extend(res[i])
        return arr
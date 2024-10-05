class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxH = 0
        res = []
        for i in range(len(heights) - 1, -1 , -1):
            if heights[i] > maxH:
                res.append(i)
                maxH = heights[i]
        res.reverse()
        return res
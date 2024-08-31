class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height) - 1
        while l < r:
            w = r - l
            res = max(res, min(height[l], height[r]) * w)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res

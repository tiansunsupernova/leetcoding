class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = []
        r_max = []
        m, n = 0, 0
        for i in range(len(height)):
            x = height[i]
            y = height[len(height) - 1 - i]
            m = max(x, m)
            n = max(y, n)
            l_max.append(m)
            r_max.append(n)
        r_max.reverse()
        res = 0
        for i in range(len(height)):
            res += max(0, min(l_max[i], r_max[i]) - height[i])
        return res
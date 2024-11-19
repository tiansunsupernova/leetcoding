class Solution:
    def __init__(self):
        self.res = 0
        self.zeroes = []
        self.ones = []
        self.len = None

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.zeroes = [s.count('0') for s in strs]
        self.ones = [s.count('1') for s in strs]
        self.len = len(strs)

        return self.dp(self.len - 1, m, n)
    
    @lru_cache(None)
    def dp(self, i, m, n):
        if m < 0 or n < 0:
            return float('-inf')  # Return negative infinity to indicate an invalid path
        if i < 0:
            return 0
        res = self.dp(i - 1, m, n)
        if m >= self.zeroes[i] and  n >= self.ones[i]:
            res = max(res, self.dp(i - 1, m - self.zeroes[i], n - self.ones[i]) + 1)
        return res
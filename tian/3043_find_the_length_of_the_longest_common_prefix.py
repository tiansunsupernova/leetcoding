class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        seen = set()
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                seen.add(s[:i])
        res = 0
        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                if s[:i] in seen:
                    res = max(res, i)
        return res
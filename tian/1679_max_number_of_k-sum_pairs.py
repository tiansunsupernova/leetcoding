class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cache = {} # k = number, v = cnt
        op = 0
        for num in nums:
            target = k - num
            if target in cache and cache[target] > 0:
                cache[target] -= 1
                op += 1
            else:
                if num not in cache:
                    cache[num] = 0
                cache[num] += 1
        return op

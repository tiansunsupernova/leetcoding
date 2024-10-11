class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt = 0
        last = 0
        for x in arr:
            cnt =  cnt + (x - last - 1)
            if cnt >= k:
                return x - 1 - (cnt - k)
            last = x
        return x + k - cnt


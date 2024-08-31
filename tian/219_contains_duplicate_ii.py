class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        di = {} # k = number, v = index
        for i,v in enumerate(nums):
            if v in di:
                j = di[v]
                if i - j <= k:
                    return True
            di[v] = i
        return False
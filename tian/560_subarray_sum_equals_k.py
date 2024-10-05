class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # k = csum(i) - csum(j) -> csum(j) = csum(i) - k
        di = {0: 1} # k = cums(i), v = cnt
        csumi, cnt = 0, 0
        for i, val in enumerate(nums):
            csumi += val
            csumj = csumi - k
            if csumj in di: cnt += di[csumj]
            di[csumi] = di.get(csumi, 0) + 1 
        return cnt

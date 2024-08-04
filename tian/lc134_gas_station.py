class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res, total, cur, n = 0, 0, 0, len(gas)
        
        for i in range(n):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            
            if cur < 0:
                cur = 0
                res = i + 1
        
        return res if total >= 0 else -1

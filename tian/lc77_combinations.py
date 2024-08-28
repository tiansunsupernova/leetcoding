class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def btrack(cur: List[int], i:int):
            if len(cur) == k:
                res.append(cur[:])
                return
            
            need = k - len(cur)
            remain = n - i + 1
            available = remain - need

            for num in range(i, i + available + 1):
                    cur.append(num)
                    btrack(cur, num + 1)
                    cur.pop()
        
        res = []
        btrack([], 1)
        return res
    

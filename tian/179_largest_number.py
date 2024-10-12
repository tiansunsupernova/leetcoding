class Num:
    def __init__(self, val):
        self.val = str(val)
    
    def __lt__(self, other):
        return self.val + other.val > other.val + self.val

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        cur = []
        for x in nums:
            cur.append(Num(x))
        cur.sort()
        res = []
        for x in cur:
            res.append(x.val)
        if res[0][0] == '0': return "0"
        return ''.join(res)
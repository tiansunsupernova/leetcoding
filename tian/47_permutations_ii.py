class Solution:
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.btrack(Counter(nums), [], len(nums))
        return self.res
    
    def btrack(self, counter, cur, l):
        if len(cur) == l:
            self.res.append(list(cur))
            return
        
        for key in counter.keys():
            if counter[key] > 0:
                cur.append(key)
                counter[key] -= 1
                self.btrack(counter, cur, l)
                counter[key] += 1
                cur.pop()

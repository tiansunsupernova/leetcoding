class SparseVector:
    def __init__(self, nums: List[int]):
        self.di = {}
        for i, val in enumerate(nums):
            if val != 0: self.di[i] = val
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        idxs = self.di.keys() & vec.di.keys()
        res = 0
        for idx in idxs:
            res += self.di[idx] * vec.di[idx]
        return res
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
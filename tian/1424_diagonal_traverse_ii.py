class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows = len(nums)
        di = defaultdict(list) # k = i + j, v = list of items
        ans = []
        for i in range(rows):
            for j in range(len(nums[i])):
                di[i+j].append(nums[i][j])
        for idx in di.keys():
            cur = reversed(di[idx])
            if cur is not None: 
                ans.extend(cur)
        return ans


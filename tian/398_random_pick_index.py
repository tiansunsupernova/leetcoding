class Solution:

    def __init__(self, nums: List[int]):
        self.di = defaultdict(list) # k = val, v = idx
        for i, v in enumerate(nums):
            self.di[v].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.di[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_rob = [0 for _ in range(n)]
        dp_not_rob = [0 for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp_rob[i] = nums[i]
                dp_not_rob[i] = 0
            elif i == 1:
                dp_rob[i] = nums[i]
                dp_not_rob[i] = dp_rob[i - 1]
            else:
                dp_rob[i] = max(dp_not_rob[i - 1], dp_rob[i - 2]) + nums[i]
                dp_not_rob[i] = max(dp_rob[i - 1], dp_not_rob[i - 1])
        
        return max(dp_rob[n - 1], dp_not_rob[n - 1])

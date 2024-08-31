class Solution:
    def jump(self, nums: List[int]) -> int:

        # Slow Implementation
        # steps = [len(nums) for _ in range(len(nums))]
        # steps[0] = 0
        # for i in range(len(nums)):
        #     for j in range(nums[i] + 1):
        #         k = i + j
        #         if k < len(nums):
        #             steps[k] = min(steps[k], steps[i] + 1)
        # return steps[len(nums) - 1]

        #
        cnt, cur_min, cur_max = 0, 0, 0

        for i in range(len(nums) - 1):
            cur_max = max(cur_max, i + nums[i])

            if i == cur_min:
                cnt += 1
                cur_min = cur_max
        
        return cnt
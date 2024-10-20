class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # - - - N X M - - -
        nums.sort()
        diff = float('inf')
        n = len(nums)
        for j in range(1, n - 1):
            i = j - 1
            k = j + 1
            while k < n and i >= 0:
                cur = nums[i] + nums[j] + nums[k]
                if abs(target - cur) < diff:
                    diff = abs(target - cur)
                    ans = cur
                if cur == target:
                    return cur
                elif cur < target:
                    k += 1
                else:
                    i -= 1
        return ans

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cnt = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                cnt = 1
                while cur + 1 in num_set:
                    cur += 1
                    cnt += 1
                max_cnt = max(max_cnt, cnt)
        return max_cnt
    
# Time: O(n) 
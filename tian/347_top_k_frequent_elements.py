class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        unique_nums = []
        for num in nums:
            if num not in di:
                di[num] = 0
                unique_nums.append(num)
            di[num] += 1
        unique_nums.sort(key = lambda x: -di[x])
        return unique_nums[:k]
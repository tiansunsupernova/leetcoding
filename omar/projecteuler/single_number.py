class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for num in nums:
            num_dict[num] = 1 + num_dict.get(num, 0)

        for n in num_dict:
            if num_dict.get(n, 0) == 1:
                return n

    # Much simpler answer users Xor.

    # class Solution:
    #     def singleNumber(self, nums: List[int]) -> int:
    #         answer = 0
    #         for num in nums:
    #             answer ^= num
    #         return answer

class Solution(object):

    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        result = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                result.append(nums[i])

        nums[:] = result # replace all elements in num list with elements in result
        return len(nums)

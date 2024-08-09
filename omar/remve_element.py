class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Create a higher function that returns true if a number isn't equal to val
        def is_not_val(element):
            return element != val

        # Use the filter function to filter out the elements equal to val
        nums[:] = list(filter(is_not_val, nums))
        return len(nums)

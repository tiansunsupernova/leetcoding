class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        intersect = set1 & set2
        ans1 = [ x for x in set1 if x not in intersect]
        ans2 = [ x for x in set2 if x not in intersect]
        return [ans1, ans2]
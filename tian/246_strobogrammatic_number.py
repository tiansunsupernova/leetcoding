class Solution:
    # 1 2 3 4 5 6 7 8 9 0

    # 1 8 0
    # 6 9
    def isStrobogrammatic(self, num: str) -> bool:
        start, end = 0, len(num) - 1
        nums = set(['1','8','0'])
        while start <= end:
            if (num[start] == '6' and num[end] == '9' or
            num[start] == '9' and num[end] == '6' or
            (num[start] in nums and num[end] in nums and num[start] == num[end])):
                start += 1
                end -= 1
            else:
                return False
        return True
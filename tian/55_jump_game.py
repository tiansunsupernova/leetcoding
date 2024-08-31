class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        rightMostGood = 0
        for i in range(0, lastPos):
            print(str(i) + "    " + str(rightMostGood))
            if rightMostGood >= i:
                if rightMostGood < i + nums[i]:
                    rightMostGood = i + nums[i]
        return rightMostGood >= lastPos
        


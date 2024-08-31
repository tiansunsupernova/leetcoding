from typing import List


def majorityElement(self, nums: List[int]) -> int:
    cnt = 1
    candidate = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == candidate:
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
            else:
                candidate = nums[i]
    return candidate
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                slow +=1
        return nums

nums = [0,1,0,3,12]
sol = Solution()
sol.moveZeroes(nums)
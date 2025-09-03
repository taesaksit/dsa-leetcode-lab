from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            for j in range(size):
                if nums[i] + nums[j] == target and i!=j:
                    return i,j


nums = [3,2,3]
target = 9
sol = Solution()
result = sol.twoSum(nums,target)
print(result)
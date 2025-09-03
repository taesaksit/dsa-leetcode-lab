from typing import List, Tuple


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[index] = nums[j]
                index += 1

        return index


nums = [3, 2, 2, 3]
val = 3
sol = Solution()
result = sol.removeElement(nums, val)

print(result)
print(nums)

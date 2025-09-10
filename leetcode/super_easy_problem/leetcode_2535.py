from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total = sum(nums)
        total_digit = 0

        for num in nums:
            for digit in str(num):
                total_digit = int(digit) + total_digit

        return abs(total - total_digit)


nums = [1, 15, 6, 3]
sol = Solution()
result = sol.differenceOfSum(nums)

print(result)

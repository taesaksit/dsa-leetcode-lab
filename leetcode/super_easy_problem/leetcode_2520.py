class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for ch in str(num):
            digit = int(ch)
            if digit != 0 and num % digit == 0:
                count += 1

        return count


nums = 121
sol = Solution()
result = sol.countDigits(nums)
print(result)
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit_list = list(map(int, str(n)))
        total = sum(digit_list)
        multiply = 1

        for i in digit_list:
            multiply = multiply * i

        return multiply - total


sol = Solution()
result = sol.subtractProductAndSum(234)
print(result)
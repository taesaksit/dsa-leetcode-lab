class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        even = 0
        odd = 0

        for i in range(1,n+1):
            if i % m == 0:
                even = even + i
            else:
                odd = odd + i
        return odd - even



sol = Solution()
result = sol.differenceOfSums(n=5,m=1)
print(result)
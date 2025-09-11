from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = 0

        for i in accounts:
            s = sum(i)
            if s > total:
                total = s
        return total



accounts = [[1,5],[7,3],[3,5]]

sol = Solution()
result = sol.maximumWealth(accounts)
print(result)
from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in hours:
            if i >= target:
                count += 1

        return count


target = 2
hours = [0, 1, 2, 3, 4]
sol = Solution()
result = sol.numberOfEmployeesWhoMetTarget(hours=hours, target=target)
print(result)
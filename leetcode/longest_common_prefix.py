from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return  ""
        prefix = strs[0]
        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


sol = Solution()
case1 = ["flower","flow","flight"]
case2 = ["dog", "racecar", "car"]
case1Result = sol.longestCommonPrefix(case1)
case2Result = sol.longestCommonPrefix(case2)
print(case1Result)
print(case2Result)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        size = n-m+1

        for i in range(size):
            print(haystack[i:i+m])
            if haystack[i:i+m] == needle:
                return i
        return -1


haystack = "sadbutsad"
needle = "sad"

sol = Solution()
sol.strStr(haystack,needle)

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
       
       size = len(s)
       
       for i in range(size // 2):
            left = i
            right = size - 1 - i
            s[left], s[right] = s[right] , s[left]
            
       print(s)

s = ["H","a","n","n","a","h"]

sol =  Solution()
sol.reverseString(s)

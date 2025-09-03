class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        s = list(word)
        
        left = 0
        right = index
        
        while left < right:
             
             temp = s[left]
             s[left] = s[right]
             s[right] = temp
             
             left +=1
             right -=1
        
        return s
        
word = "abcdefd"
ch = "d"
sol = Solution()
sol.reversePrefix(word, ch)
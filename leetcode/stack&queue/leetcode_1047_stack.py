class Solution:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
         self.stack.append(data)
    
    def pop(self):
        self.stack.pop()
        
    
    def removeDuplicates(self, s: str) -> str:

        for char in s:
            if self.stack and self.stack[-1] == char:
                self.pop()
            else :
                self.push(char)
        return ''.join(self.stack)

s = "azxxzy"
sol = Solution()
result =sol.removeDuplicates(s)

print(result)
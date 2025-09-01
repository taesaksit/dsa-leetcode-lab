from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        self.stack = [] 

        # + = sum previous two score
        # D = Double previous score
        # C = remove
        
        for op in operations:
            if op == '+':
                if len(self.stack)  >= 2:
                    self.stack.append(self.stack[-2] + self.stack[-1])
            elif op == 'D':
                if len(self.stack) >= 1:
                    self.stack.append(self.stack[-1] * 2)
            elif op == 'C':
                if self.stack:
                    self.stack.pop()
            else :
                self.stack.append(int(op))
        
        
        return sum(self.stack) 
                    
                


 

ops = ["5","2","C","D","+"]

sol = Solution()
sol.calPoints(ops)
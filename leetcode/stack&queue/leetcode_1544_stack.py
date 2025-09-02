class Solution:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return
        self.stack.pop()

    def makeGood(self, s: str) -> str:

        for char in s:
            if self.is_empty():
                self.push(char)
            else:
                if char.lower() == self.stack[-1].lower() and char != self.stack[-1]:
                    self.pop()
                else:
                    self.push(char)

        return "".join(self.stack)


input = "leEeetcode"
sol = Solution()
print(sol.makeGood(input))

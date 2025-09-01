class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for char in s :
            if char in mapping:
                if not stack:
                    return False
                if stack:
                    top_element = stack.pop()
                    if(mapping[char] != top_element):
                        return False
            else :
                stack.append(char)
        print(len(stack))
        return len(stack) == 0


inputs = ")[]{}"
sol = Solution()
print(sol.isValid(inputs))

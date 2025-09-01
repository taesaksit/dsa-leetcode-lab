class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        self.stack_a = []
        self.stack_b = []

        # ----- ทำงานกับ s -----
        for a in s:
            if a == "#":
                if self.stack_a:   # กัน pop บน stack ว่าง
                    self.stack_a.pop()
            else:
                self.stack_a.append(a)

        # ----- ทำงานกับ t -----
        for b in t:
            if b == "#":
                if self.stack_b:
                    self.stack_b.pop()
            else:
                self.stack_b.append(b)

        # ----- เปรียบเทียบผลลัพธ์ -----
        print(self.stack_a, self.stack_b)
        return self.stack_a == self.stack_b


# ✅ ทดสอบ
sol = Solution()
s = "a"
t = "b"
print(sol.backspaceCompare(s, t))  # True

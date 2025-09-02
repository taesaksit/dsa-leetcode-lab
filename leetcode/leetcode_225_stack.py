from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()  
        self.q2 = deque() 

    def push(self, x: int) -> None:
       
        self.q2.append(x)

        while self.q1:
            pop_data = self.q1.popleft()
            self.q2.append(pop_data)


        # move q2 -> q1
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0

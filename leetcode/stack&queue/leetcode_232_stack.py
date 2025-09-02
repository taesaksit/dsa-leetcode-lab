class MyQueue:

    def __init__(self):
        self.stack = []
        self.queue = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return
        
        if len(self.queue) == 0 :
            for i in range(len(self.stack)):
                pop_data = self.stack.pop()
                self.queue.append(pop_data)
            
        return self.queue.pop()
        

    def peek(self) -> int:
        if self.empty():
            return None
        if len(self.queue) == 0:
            while self.stack:
                pop_data = self.stack.pop()
                self.queue.append(pop_data)

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.queue) == 0

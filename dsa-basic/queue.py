from collections import deque


class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.q.popleft()

    def is_empty(self):
        return len(self.q) == 0

    def front(self):
        if self.is_empty():
            return None
        return self.q[0]

    def size(self):
        return len(self.q)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("size:", q.size())
print("font:", q.front())

print()
q.dequeue()

print("size:", q.size())
print("front:", q.front())

class Stack:
    def __init__(self, max=10):
        self.max = max
        self.stack = [None] * max
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max - 1

    def push(self, data):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top = self.top + 1
        self.stack[self.top] = data

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return
        self.stack[self.top] = None
        self.top = self.top - 1
        print("Data pop: ", self.stack[self.top])

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None

        peek_data = self.stack[self.top]
        print(peek_data)
        return peek_data

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            for i in range(self.max):
                print(f"Index:{i} => {self.stack[i]}")
            print("=" * 40)

            for i in range(self.top, -1, -1):
                print(f"Index:{i} => {self.stack[i]}")
            print("=" * 40)


st = Stack()

for i in range(1, 12):
    st.push(i)

st.display()

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()

    def add(self,data):
        new_node = Node(data)
        current = self.head

        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete(self, data):
        current = self.head.next
        while current is not None:
            if data == current.data:
                if current.prev:
                    current.prev.next = current.next #เอา Node ก่อนหน้า ---> Node ถัดไป
                if current.next:
                    current.next.prev = current.prev #เอา Node ถัดไป <-- ชี้ไป Node ก่อนหน้า
            current = current.next

    def display_forward(self):
        print('Forward')
        current = self.head.next
        while current is not  None:
            print(current.data , end=" <-> " if current.next  else "")
            current = current.next
        print()

    def display_backward(self):

        print('Backward')
        current = self.head.next
        # ไปจนถึงตัวสุดท้าย
        while current.next is not None:
            current = current.next
        # ถอยหลัง
        while current is not self.head:
            print(current.data, end=" <-> " if current.prev != self.head  else "")
            current = current.prev



dl = DoubleLinkedList()

dl.add(10)
dl.add(20)
dl.add(30)

dl.display_forward()
dl.display_backward()
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    # Add
    def add(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    # Delete
    def delete(self,data):
        # have data ?
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next # head → 30 → 300 → 400 → None # เปลี่ยนจากชี้ไปที่ 300 → ชี้ไปที่ 400

            else:
                current = current.next # move poiter

    def display(self):
        current = self.head
        while current.next is not None:
            print(f'[{current.data} {id(current.next)} ]---->')
            current = current.next
        print(f'[{current.data} {current.next}]')

ll = LinkedList()
ll.add(30)
ll.add(300)
ll.add(400)
ll.display()
print()
ll.delete(300)
ll.display()
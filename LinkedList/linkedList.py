class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def traverse(self):
        if self.head is None:
            print("Null")
            return
        current = self.head
        while current is not None:
            print(f"{current.data} -->", end = " ")
            current = current.next
        print("Null")
    
    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        i = 0
         





list1 = LinkedList()
list1.insert_at_end(10)
list1.insert_at_end(20)
list1.insert_at_beginning(5)
list1.insert_at_index(2, 0)
list1.traverse()

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

    def traverse(self):
        if self.head is None:
            print("Null")
            return
        current = self.head
        while current is not None:
            print(f"{current.data} -->", end = " ")
            current = current.next
        print("Null")

list1 = LinkedList()
list1.insert_at_end(10)
list1.traverse()

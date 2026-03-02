class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def del_front(self):
        if self.head == None:
            print("empty list")
            return
        self.head = self.head.next

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

l = LinkedList()
l.insert_beg(5)
l.insert_beg(10)
l.del_front()
l.display()
## Linked List  

# It is a data structure that contains a sequence of elements.nodes are linked to each other. 

# Node is a data structure that contains a value and a pointer to the next node. 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    

class LinkedList:
    def __init__(self):
        self.head = None

# insert at the front

    def insert_beg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# insert at end

    def insert_end(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next=new_node

    def insert_pos(self,data,pos):
        if pos < 1:
            print("invalid position")
            return
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for i in range(pos-2):
            if temp == None or temp.next == None:
                print("Invalid Position")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

l = LinkedList()
l.insert_beg(5)
l.insert_end(10)
l.insert_pos(20,2)
l.display()
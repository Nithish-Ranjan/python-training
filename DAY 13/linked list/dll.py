class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None    

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self,data):
        new_node = Node(data)
        new_node.right = self.head
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return 
        
        temp =self.head
        while temp.right != None:
            temp = temp.right
        temp.right = new_node

    def insert_pos(self,data,pos):
        new_node = Node(data)
        if pos < 1:
            print("invalid pos")
            return
        if pos == 1:
            insert_beg(data)
            return
        temp = self.head
        for i in range(pos-2):
            if temp ==  None or temp.right == None:
                print("invalid pos")
                return
            temp = temp.right
        new_node.right = temp.right
        temp.right = new_node

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end="->")
            temp = temp.right
        print("None")

    def del_front(self):
        if self.head == None:
            print("empty list")
            return
        self.head = self.head.right

    def del_end(self):
        if self.head == None:
            print("empty list")
            return
        temp = self.head
        tem = self.head
        while temp.right != None:
            tem = temp
            temp = temp.right
        tem.right = None
        # temp.left = None

l = LinkedList()
l.insert_beg(5)
l.insert_end(20)
l.insert_end(10)
l.insert_pos(30,2)
# l.del_front()
# l.del_end()
l.display()
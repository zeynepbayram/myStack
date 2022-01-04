from Node import Node
class myStack:
    def __init__(self, data = None):
        if data != None:
            self.head = Node(data)
        else:
            self.head = None
    
    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def pop(self):
        temp = self.head.data
        self.head = self.head.next
        return temp

    def empty(self):
        return self.head == None
    
    def top(self):
        if self.head == None:
            return None
        return self.head.data
    
    def printStack(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end = " ")
            temp = temp.next


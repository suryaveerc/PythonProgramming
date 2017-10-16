class Node:
    def __init__(self,data):
        self.next = None
        self.previous = None
        self.data = data
    
    def getData(self):
        return self.data
    
    def setData(self,data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious

    def getPrevious(self):
        return self.previous

class LinkedList:
   
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def isempty(self):
        return self.head is None

    def addNode(self,item):
        print("Current length is : ", self.length)
        if not self.isempty():
            print("adding to non empty list")
            curr = Node(item)
            self.tail.next = curr
            curr.prev = self.tail
            self.tail = curr
            self.length += 1
        else:
            print("Creating new list")
            curr = Node(item)
            self.head = curr
            self.tail = curr
            self.length += 1 
            
    def display(self):
        curr = self.head
        for _ in range(self.length):
            print(curr.getData())
            curr = curr.next
            
 
 
 
 
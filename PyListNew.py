
class PyList:
    def __init__(self, contents=[], length=10):
        self.items = [None] * length
        self.numItems = 0
        self.size = length
        
        for e in contents:
            self.append(e)
    
    def __getitem__(self,index):
        if index < self.numItems:
            return self.items[index]
        
        raise IndexError("Pylist index out of range")
    
    def append(self, item):
        if self.numItems == self.size:
            self.__expand()
        
        self.items[self.numItems] = item
        self.numItems += 1
        
    def __setitem__(self, index, item):
        if index >= self.numItems:
            raise IndexError("Given index out of bounds")
        self.items[index] = item
    
    
    def __add__(self, otherList):
        
        newList = PyList()
        
        for i in range(self.numItems):
            newList.append(self.items[i])

        for i in range(otherList.numItems):
            newList.append(otherList.items[i])
        return newList
        
    def __expand(self):
        size = self.size + self.size//2 + 1
        self.size = size
        newList = PyList(self.items, self.size)
        self.items  = newList.items
        
    def insert(self, index, item):
        if self.numItems == self.size:
            self.__expand()
            
        if index < self.numItems:
            for i in range(self.numItems-1, index-1, -1):
                print("Current index: " + str(i) + " Value: " + str(self.items[i]))
                self.items[i+1] = self.items[i]
            self.items[index] = item
            self.numItems += 1
        elif index == self.numItems:
            self.append(item)
        else:
            raise IndexError("Index out of bounds")
        
    def __delitem__(self, index):
        if index < self.numItems:
            for i in range(index, self.numItems-1):
                self.items[i] = self.items[i+1]
            self.items[self.numItems-1]  = None
            self.numItems -= 1
            
        else:
            raise IndexError("Index out of bound")
    
    def __eq__(self,otherList):
        if type(self) != type(otherList):
            return False
        if self.numItems != otherList.numItems:
            return False
        
        for i in range(self.numItems):
            if self.items[i] != otherList[i]:
                return False
        return True
    
    def __iter__(self):
        for i in range(self.numItems):
            yield(self.items[i])
    
    def __len__(self):
        return self.numItems
    
    def __contains__(self, item):
        for i in range(self.numItems):
            if item == self.items[i]:
                return True
        return False
    
    def __str__(self):
        s = "["
        for i in range(self.numItems):
            s += str(self.items[i])
            if i < self.numItems-1:
                s += ","
            else:
                s += "]"
        return s

    def __repr__(self):
        s = "PyList(["
        for i in range(self.numItems):
            s = s + str(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "])"
        return s     
    def sort(self):
        pass

b = PyList([1,2,3],3)
a = PyList(["a","b"],2)
print("Number of items in A: ", end = "")
print(a.numItems)
print("List of items in A: ", end = "")
print(a.items)
print("Appending item in A")
a.append("c")
print("Number of items in list A after append: ", end="")
print(a.numItems)
print("List A after append: ", end="")
print(a.items)
print("Adding list b to a")
c= a+b

print("New list after adding a and b: ", end="")
print(c.items)
c.insert(6,"as")
print("List after insert: ", end="")
print(c.items)
print("Number of items in list A after insert: ", end="")
print(c.numItems)
del c[2]
print("List after delete: ", end="")
print(c.items)
print("Is list a==b: ", a==b)
print("Printing elements using iterator")
for i in c:
    print(i)

print("Does list contains 4 ?", 4 in c)
print(c)
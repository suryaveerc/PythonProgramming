
class Clearable:
    def __init__(self):
        self.list = [None] * 10
        self.count = 0
    def __getitem__(self, index):
        print(self.list[index])
        if self.list[index] != None:
            return self.list[index]
        else:
            return None
    def __len__(self):
        return self.count
    
    def append(self, item):
        if self.count == len(self.list):
            self.list = [None] * 10
            self.count = 0
        
        self.list[count] = item
        self.count += 1

a = Clearable()
print("hello")
print("length of a " + str(len(a)))
print(a[0])
        
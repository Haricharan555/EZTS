class Q:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        self.items.pop(0)
    def size(self):
        return len(self.items)
    
s=stack()
s.push(10)
s.push(20)
print(s.items)
s.pop()
print(s.items)
s.size()
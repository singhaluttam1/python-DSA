class stack(list):
    def is_empty(self):
       return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            super().pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("No attribute 'insert' in stack" )
s1=stack()
# s1.insert(0,10)
s1.push(12)
s1.push(13)
s1.push(14)
s1.push(15)
print("top value=",s1.peek())
s1.pop()
print("top value=",s1.peek())
print()
        
        
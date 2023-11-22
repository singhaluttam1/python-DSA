class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class CLL:
    def __init__(self,last=None):  
        self.last=last
    def isempty(self):
        return self.last==None
    def insert_at_start(self,data):
        n=Node(data)
        if self.isempty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n  
    def insert_at_last(self,data):
        n=Node(data)
        if self.isempty():
            n.next=n
            self.last=n  
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
    def search(self,data): 
        if self.isempty():
            return None
        temp=self.last.next
        while temp !=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
            if temp.item==data:
                return temp
        return None
    def print_list(self):
        if not self.isempty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=" ")
            temp=temp.next
            print(temp.item)
    def delete_first(self,data):
        if not self.isempty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                self.last.next=temp.next

    def delete_last(self,data):
        if not self.isempty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                    temp.next=self.last.next
                    self.last=temp

    def delete_item(self,data):
        if not self.isempty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
            else:
                if self.last.next==data:
                    self.delete_first()
                else:
                    temp=self.last.nextt                     
                    while temp.next!=self.last: 
                        if temp.next==self.last:
                            if self.last.item==data:
                                self.delete_last()
                            # temp.next.next=self.last.nex
                        if temp.next.item==data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next
    def __iter__(self):
        if self.last==None:
            return CLLIterator(None) 
        else:
            return CLLIterator(self.last.next)
class CLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data
cll=CLL()
cll.insert_at_start(10)
cll.insert_at_start(12)
cll.insert_at_last(20)
cll.insert_at_last(30)
cll.insert_after(cll.search(20),34)
for x in cll:
    print(x)
print()




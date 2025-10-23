class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=newnode
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end="->")
            current=current.next
        print("None")
    def reversenode(self):
        prev=None
        current=self.head
        while(current is not None):
            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode
        self.head=prev
    def deletenode(self,value):
        current=self.head
        prev=None
        if current is not None and current.data==value:
            self.head=current.next
            return
        while current is not None and current.data!=value:
            prev=current
            current=current.next
        if current is None:
            print("Value not found")
            return
        prev.next=current.next
    def deletenodebyindex(self,index):
        current=self.head
        if index==0:
            self.head=current.next
            return
        while current is not None and count!=index:
            prev=current
            current=current.next
            count+=1
        if current is None:
            print("Index is out of range")
            return 
        prev.next =current.next
    def checkingcycle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    def makingcycle(self):
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=self.head.next
ll=linkedlist()
ll.append(10)
ll.append(20)
ll.display()
ll.reversenode()
ll.display()
ll.deletenodebyindex(0)
ll.display()
ll.append(20)
ll.append(10)
ll.display()
ll.makingcycle()
check=ll.checkingcycle()
print(check)
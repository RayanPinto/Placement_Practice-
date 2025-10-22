class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        current=self.head
        while(current.next is not None):
            current=current.next
        current.next=newnode
    def display(self):
        current=self.head
        while(current is not None):
            print(current.data,end="->")
            current=current.next
        print("None")
l=linkedlist()
l.append(20)
l.append(30)
l.display()
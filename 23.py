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
    def delete(self,value):
        current=self.head
        if current is not None and current.data==value:
            self.head=current.next
            return
        prev=None
        while current is not None and current.data!=value:
            prev=current
            current=current.next
        if current is None:
            print("value not found")
            return
        prev.next=current.next
    def reversenode(self):
        current=self.head
        prev=None
        while current is not None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev
            
            
        
l=linkedlist()
l.append(20)
l.append(30)
l.display()
l.reversenode()
l.display()
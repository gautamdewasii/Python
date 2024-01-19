class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLL:
    def __init__(self):
        self.head=None
    
    def insert_at_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    
    def insert_at_pos(self,data,pos):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node

    
    def deletion_at_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    
    def deletion_at_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next:
            temp=temp.next
            prev=prev.next
        prev.next=None

    def deletion_at_pos(self,pos):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        temp.next=temp.next.next

    def display(self):
        temp=self.head
        if self.head is None:
            print("empty list")
        while temp:
            print(temp.data," --> ",end=" ")
            temp=temp.next
    
n1=Node(20)
link=SinglyLL()
link.head=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
link.display()
print("\n")
link.insert_at_beg(10)
link.insert_at_end(50)
link.insert_at_pos(25,2)
link.display()
print('\n')
link.deletion_at_pos(3)
link.display()
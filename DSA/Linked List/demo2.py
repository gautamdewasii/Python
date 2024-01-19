class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.head=None
    
    def insert_at_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    
    def insert_at_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp

    def insert_at_pos(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.prev=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node

    def deletion_at_beg(self):
        temp=self.head
        self.head=temp.next
        self.head.prev=None
        temp.next=None


    def deletion_at_end(self):
        temp=self.head.next
        pre=self.head
        while temp.next:
            temp=temp.next
            pre=pre.next
        pre.next=None
        temp.prev=None

    def deletion_at_pos(self,pos):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        temp.next=temp.next.next
        temp.next.prev.prev=None
        temp.next.prev=temp

    def display(self):
        temp=self.head
        if self.head is None:
            print("Linked list is empty")
        while temp:
            print(temp.data," -->",end=" ")
            temp=temp.next
        print(end="\n")
        
    def reverse(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data," --> ",end=" ")
            temp=temp.prev

n1=Node(10)
link=DLL()
link.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
link.display()
link.reverse()
link.insert_at_beg(5)
link.insert_at_end(40)
link.insert_at_pos(3,25)
print("\n")
link.display()
link.reverse()
print("\n")
link.deletion_at_beg()
link.deletion_at_end()
link.deletion_at_pos(1.)
link.display()
link.reverse()
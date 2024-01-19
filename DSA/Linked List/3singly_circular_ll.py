# Class for creating nodes of SinglyCLL
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
class Node:
    # constructor for initializing nodes 
    def __init__(self,data):
        # value of node
        self.data=data
        # next pointer pointing for next node o SinglyCLL
        self.next=None
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# class for creating 'head' and 'tail' of SCLL
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
class SinglyCLL:
    # constructor for initializing 'head' and 'tail' of SCLL
    def __init__(self):
        # for pointing towards first node of SCLL
        self.head=None
        # for pointing towards last node of SCLL
        self.tail=None
    
    # INSERTION OPERATIONS :-
    # *********************************************************************
    # inserting at the beginning of LL:-
    def insertAtBeg(self,data):
        # creating new node with value=data
        newNode=Node(data)
        
        # if list is empty
        if self.head is None:
            # head and tail pointing to same node , because linked list contains only 1 node
            self.head=newNode
            self.tail=newNode
            self.tail.next=self.head
        else:
            # 'next' node of newNode pointing to PAST 1ST node 
            newNode.next=self.head
            # updating head with newNode
            self.head=newNode
            # updating tail's next with new Head
            self.tail.next=self.head
    
    # inserting at the end of Ll:-
    def insertAtEnd(self,data):
        # creating newNode
        newNode=Node(data)
        # if list is empty
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.tail.next=self.head
        else:
            # updating last node's 'next' pointer with newNode
            self.tail.next=newNode
            # updating tail with newNode ( last element)
            self.tail=newNode
            # pointing last node's 'next' pointer to head
            self.tail.next=self.head

    # insert at any position ( form 0th index to nth index )
    def insertAtPos(self,data,pos):
        # creating new node 
        newNode=Node(data)
        # initializing new member self.'pos' with value of 'pos'
        self.pos=pos
        # if list is empty
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.tail.next=self.head
        else:
            # if need to insert at the beginning
            if pos==0:
                # calling insertAtBeg() member function
                self.insertAtBeg(data)
            else:
                # temp for iterate to linked list nodes
                temp=self.head
                # until temp equals to 'pos-1' index node
                # means previews node of target pos node  ( note pos starts from 0th index) 
                for i in range(pos-1):
                    # updating temp
                    temp=temp.next
                # new node 'next' pointer pointing to pos index node
                newNode.next=temp.next
                # previews node of pos index node , pointing to newNode
                temp.next=newNode
    # ***************************************************************************

    # DELETION OPERATIONS :-
    # ****************************************************************************

    # deleting node from the beginning of ll
    def deletionAtBeg(self):
        # if linked list is empty
        if self.head is None:
            print("linked list is empty...")
        else:
            # if contains only one node
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head
                self.head=temp.next  # or =self.head.next
                temp.next=None
                self.tail.next=self.head
    # deleting node from the end of ll
    def deletionAtEnd(self):
        # if list is empty
        if self.head is None:
            print("linked list is empty...")
        else:
            # is list contains only one node
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head.next
                while temp.next!=self.tail:
                    temp=temp.next
                self.tail=None
                self.tail=temp
                temp.next=self.head
    # deleting node from any position of linked list
    def deletionAtPos(self,pos):
        # if node is empty
        if self.head is None:
            print("linked list is empty...")
        else:
            # if list contains one node
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head.next
                prev=self.head
                self.pos=pos
                for i in range(pos-1):
                    temp=temp.next
                    prev=prev.next
                prev.next=temp.next
                temp.next=None
        
    def search(self):
        data=int(input("enter any value for searching operation :-  "))
        temp=self.head
        count=0
        flag=0
        while temp!=self.tail:
            if data==temp.data:
                flag=1
                break
            temp=temp.next
            count+=1
        if data==temp.data:
            flag=1
        if flag==1:
            print("data found in linked list at index ",count)

    # **************************************************************************** 


    # DISPLAY FUNCTION
    # ***************************************************************************
    # iterating from head to tail of SCLL
    def display(self):
        
        # temp used for iteration
        temp=self.head
        # if list is empty
        if temp is None:
            print("Linked List is empty...")
        # if not empty
        else:
            # printing 1st node's value
            print(temp.data," --> ",end=" ")
            # until last node's 'next' not pointing to 'head' 
            while temp.next!=self.head:
                # updating temp with its next node
                temp=temp.next
                # printing current node's value
                print(temp.data," --> ",end=" ")
            # value of node who's pointed by last node (tail)
            print("  --> * ",temp.next.data)
    # *********************************************************************************

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# CALLING OF MEMBER FUNCTION AND CREATION OF OBJECTS 
print("Before creating any node :- ")            
h=SinglyCLL()
h.display()
print("\nAfter creating first node :- ")
n1=Node(10)
h.head=n1
h.tail=n1
h.tail.next=h.head
h.display()

print("\nAfter creating second node :- ")
n2=Node(20)
h.tail.next=n2              # or h.n1.next=n2
h.tail=n2
h.tail.next=h.head
h.display()

print("\nAfter creating multiple nodes :- ")
n3=Node(30)
h.tail.next=n3
h.tail=n3
h.tail.next=h.head
n4=Node(40)
h.tail.next=n4
h.tail=n4
h.tail.next=h.head
h.display()

print("\nAfter insertion operation at the beg and end :- ")
h.insertAtBeg(5)
h.insertAtEnd(50)
h.display()

print("\nAfter insertion operation at any position :- ")
h.insertAtPos(25,3)
h.display()


print("\nAfter deletion operation at beg and end :- ")
h.deletionAtBeg()
h.deletionAtEnd()
h.display()

print("\nAfter deletion operation at position :- ")
h.deletionAtPos(3)
h.display()

h.search()
# class used to create individual nodes of DLL
class Node:
    # constructor for initializing data members of class 'Node'
    def __init__(self,data):
        # previews pointer  ( pointing towards previews node)
        self.prev=None
        # data or value of node
        self.data=data
        # next pointer ( pointing towards next node)
        self.next=None

# class used to create link between Nodes 
# also used for other operations like insertion , deletion , iteration
class Doubly_Linked_List:
    # constructors 
    def __init__(self):
        # head ( used to point on first node of DLL)
        self.head=None

    # INSERTION OPERATIONS :-
    # ************************************************************************
    # insertion operation  ( inserting at the beginning of the DLL)
    def insertAtBeg(self,data):
        # creating node that want to insert
        newNode=Node(data)
        # next pointer of newNode will pointing to past 1st node
        newNode.next=self.head
        # preview node of past 1st node pointing to new 1st node
        self.head.prev=newNode
        # updating head with newNode 
        self.head=newNode
    
    # insertion at the end of DLL
    def insertAtEnd(self,data):
        # creating new node
        newNode=Node(data)
        # creating temporary head for iteration
        temp=self.head
        # until temp.next=None or temp is pointing to last node of DLL
        while temp.next:
            # updating temp
            temp=temp.next
        # now, temp.next pointing to new last node , newNode
        temp.next=newNode
        # newNode preview is past last node that is 'temp'
        newNode.prev=temp

    # inserting at any position of DLL
    def insertAtPos(self,data,pos):
        # creating new node
        newNode=Node(data)
        self.pos=pos
        # creating temp variable
        temp=self.head
        # until ith index will equals to last index of pos index ( 0th starting )
        for i in range(pos-1):
            temp=temp.next
        # next of 'newNode' pointing to current 'pos' index node , 'temp.next'
        newNode.next=temp.next
        # 'newNode' prev pointing to 'pos-1' index node , 'temp'
        newNode.prev=temp
        # prev of 'pos' index node pointing to newNode
        temp.next.prev=newNode
        # 'pos-1' index node next pointing to newNode 
        temp.next=newNode

    # *************************************************************************

    # DELETION OPERATIONS :-
    # ***************************************************************************
    # deleting at the beginning of the DLL
    def deletionAtBeg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
    # deleting at the end of DLL
    def deletionAtEnd(self):
        temp=self.head.next
        prev=self.head
        while temp.next:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None

    # deleting at any Position of the DLL
    def deletionAtPos(self,pos):
        self.pos=pos
        temp=self.head.next
        prev=self.head

        for i in range(pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next.prev=prev
        temp.prev=None
        temp.next=None 
    
    # ***************************************************************************


    # DISPLAY ( ITERATION ):- 
    # *************************************************************************
    # iterate to dll and display each data of nodes
    def display(self):
        # creating temporary node for iteration in dll
        temp=self.head

        # if there is no node present in DLL
        if self.head is None:
            print("empty linked list ... ")
        else:
            # iterate until temp=None
            while temp:
                # printing 'temp' node data
                print(temp.data,"-->",end=" ")  
                # updating current node 'temp' with its next node 
                temp=temp.next
            print("\n")

    # iteration operation in reverse operation
    def reverse_display(self):
        temp=self.head

        # if there is no node present in DLL
        if self.head is None:
            print("empty linked list ... (reverse search)")
        else:
            # until 'temp' pointing to last node of DLL
            while temp.next:
                temp=temp.next
            # until 'temp.prev' equals to None
            while temp:
                # printing data of each current node
                print(temp.data,"-->",end=" ")
                # updating temp with its previews node 
                temp=temp.prev 

    # ******************************************************************


print("Before any node creation :- ")
# Creating Object of Doubly_Linked_List class
h=Doubly_Linked_List()
# calling display object
h.display()
h.reverse_display()
print("\nAfter creating nodes :-")
n1=Node(10)
h.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
n5=Node(50)
n4.next=n5
n5.prev=n4
h.display()
h.reverse_display()

print("\nInsertion operation :- ")
h.insertAtBeg(5)
h.insertAtEnd(60)
h.display()
h.reverse_display()
print("\nInsert at any position")
h.insertAtPos(35,4)
h.insertAtPos(70,7)
h.display()
h.reverse_display()

print("\nDeletion operations :- ")
h.deletionAtBeg()
h.deletionAtEnd()
h.deletionAtPos(2)
h.display()
h.reverse_display()
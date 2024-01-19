# class used to create links between nodes in linked list
# it also created head , which initially pointed towards first node
class Link:
    
    # initializations of member variables
    # constructor declaration
    def __init__(self):
        # head, which pointed to the first node
        self.head=None
    
    # member function for inserting new node at the beginning
    # data is value for new node
    def insertAtBeg(self , data):
        # creating new node with data as a value 
        new_Node=Node(data)
        # connecting new_Node with first node 
        # head value inserted into 'next' of new_Node
        new_Node.next=self.head
        # updating head, pointing to new first node
        self.head=new_Node
        
    # for inserting at the end of linked list    
    def insertAtEnd(self,data):
        # creating temporary head,
        # so that no changes occurs on 'head'
        temp=self.head
        # creating new node
        new_Node=Node(data)
        # until temp.next= None
        while temp.next:
            # updating temp value , with its next node 
            temp=temp.next
        # when temp.next=None, linking it with new_Node
        temp.next=new_Node
    
    # inserting new node at any given position ( index )
    # pos = position
    def insertAtPos(self,data,pos):
        self.pos=pos
        # creating temporary head 
        temp=self.head
        # creating new node
        new_Node=Node(data)
        # loop until (pos-2)
        # NOTE:- at i=0, temp is actually equivalent to NODE_1
        # print("-------",temp.data)
        for i in range(pos-1):
            # updating temp with next node
            temp=temp.next
        
        # updating new node next with its next node,
        # which is stored in previews node's next variable
        new_Node.next=temp.next
        # updating previews node next with new node 
        temp.next=new_Node
        
    
    # DELETION OPERATIONS :-
    
    # deleting first node of the linked list :-
    def deletionAtBeg(self):
        # for current node
        temp=self.head
        # linking head to second node of the linked list
        self.head=temp.next
        # removing link b/w first node and 2nd node
        temp.next=None
        
    # deleting last element of the linked list
    def deletionAtEnd(self):
        # current node of ll
        temp=self.head.next
        # previous node of ll
        prev=self.head
        # until current node's next==None
        while temp.next is not None:
            # previous equals to current node
            prev=prev.next
            # current equals to its next node
            temp=temp.next
        # removing link b/w 2nd last node and last node
        prev.next=None
        # note :- last node's next=None , thus no need to initialize this again
    
    # deleting any specific node of ll
    def deletionAtPos(self,pos):
        # initializing position as 'pos'
        self.pos=pos
        # previous node of ll
        prev=self.head
        # current node of ll
        temp=self.head.next
        # if want to remove first node
        if pos==0:
            # linking head to the 1st index node ( current node )
            self.head=temp
            # removing link b/w previous node(0st node ) and current node ( 1st node )
            prev.next=None
            # ending this function
            return
        # until 0 to pos-2
        for i in range(0,pos-1):
            # updating with its next node
            temp=temp.next
            prev=prev.next
        # initializing previous node 'next' with current node's next
        prev.next=temp.next
        # current node's next=None ,
        #removing link b/w current and its next node
        temp.next=None
    
    
        # for display ( iterating till end of the node )
    def display(self):
        # creating temporary head 
        temp=self.head
        # if head=None means linked list is empty
        if self.head is None:
            print("LinkedLIst is Empty...")
        # until temp=None
        while temp:
            # printing value of current node
            print(temp.data)
            # updating temp with its next node
            temp=temp.next

# Node class , Blueprint for creating Node Objects in Linked list
class Node:
    
    # initialing member variables of our node
    def __init__(self,data):
        self.data=data
        self.next=None

# Initial Linked List without creating any Nodes :-
print("Initial LinkedList :- \n")
# creating head 'h' by calling Link class constructor
h=Link()

# creating first node 'n1' by calling Node class constructor
n1=Node(20)

# linking 'head' with first node of linked list
h.head=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
h.display()
# INSERTION OPERATION :-
print("After insertion operation at the beginning :-")
h.insertAtBeg(10)
h.insertAtBeg(5)
h.display()
print("After insertion operation at the end :- ")
h.insertAtEnd(60)
h.insertAtEnd(70)
h.display()
print("AFter insertion operation at any position :-")
h.insertAtPos(295,3)
h.insertAtPos(1001,6)
h.display()

# DELETION OPERATION :- 
print("\nAfter deletion operations :- ")
h.deletionAtBeg()
h.deletionAtEnd()
h.display()
print("\nAFter deletion at any position : -")
h.deletionAtPos(7)
h.display()